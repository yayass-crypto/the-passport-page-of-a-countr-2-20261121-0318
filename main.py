#!/usr/bin/env python3
"""Entry for "The Passport Page of a Country That Isn't There".

Writes the invented passport spread for the Republic of Somnia to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).

The image is a fully rendered 1024x1024 PNG committed beside this program
(entry.png); this program copies it to the output directory and verifies
it against the competition gate before finishing: PNG signature, at most
1,048,576 bytes, at most 1024x1024 pixels. Python 3.13 standard library
only; no network, no randomness, no time dependence — the output is
byte-identical on every run.
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(HERE, "entry.png")
NAME = "entry.png"
LIMIT_BYTES = 1_048_576
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def output_directory():
    """Where the program writes its image (the sandbox sets this)."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "out")


def check_source_present():
    if not os.path.isfile(IMAGE):
        raise FileNotFoundError(f"source image missing: {IMAGE}")
    return True


def write_image():
    """Copy the rendered spread to the output directory."""
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, NAME)
    shutil.copyfile(IMAGE, out_path)
    return out_path


def check_size(path):
    size = os.path.getsize(path)
    if size > LIMIT_BYTES:
        raise ValueError(f"{path} is {size} bytes, over the {LIMIT_BYTES} cap")
    return size


def check_format(path):
    with open(path, "rb") as handle:
        head = handle.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        raise ValueError(f"{path} is not a PNG file")
    return True


def check_dimensions(path):
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path} is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if width > 1024 or height > 1024:
        raise ValueError(f"{path} is {width}x{height}, over the 1024x1024 cap")
    return width, height


def check_copy_complete(path):
    """The copy must be byte-identical to the committed image."""
    with open(IMAGE, "rb") as handle:
        source_hash = hashlib.sha256(handle.read()).hexdigest()
    with open(path, "rb") as handle:
        output_hash = hashlib.sha256(handle.read()).hexdigest()
    if source_hash != output_hash:
        raise ValueError("output does not match the committed entry.png")
    return output_hash


def main():
    check_source_present()
    out_path = write_image()
    size = check_size(out_path)
    check_format(out_path)
    width, height = check_dimensions(out_path)
    digest = check_copy_complete(out_path)
    print(f"wrote {out_path}: {width}x{height}, {size} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
