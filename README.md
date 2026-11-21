# The Passport Page of a Country That Isn't There

[![make.fun](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/yayass-crypto/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/yayass-crypto/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

An invented passport spread for **the Republic of Somnia** — a country
that does not exist, where everyone is always dreaming. Entry for the
[make.fun competition](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
($50 pot, 20 places, 1st $18, free entry).

## What the image shows

An open passport on a walnut desk, with a paperclip, a gold seal, and a
boarding pass tucked underneath:

- **Data page** — coat of arms (crescent moon and three stars, motto
  *Semper in Somniis* — "Always in Dreams"), a portrait of the holder
  **Jane Anya Doe** (eyes closed, dreaming), and her details: born
  14 JUN 1998 in Slumber, Somnia; passport SOM 004213, issued
  12 MAR 2024 in Reverie, expiring 11 MAR 2034; plus a machine-readable
  zone with correct ICAO check digits and the note *"If found while the
  holder is asleep, please return it to the nearest dream."*
- **Visas page** — a visa for **the Land of Nod** (tourist, single entry,
  14 MAY – 11 AUG 2024, fee 40 ZZZ paid) with the condition *"Valid only
  while the holder is asleep"*, six arrival / departure / transit stamps
  from Somnia's neighbours — the Kingdom of Nowhere, the Land of Nod,
  Limbo, Elsewhere, and the Void — all dated after the passport was
  issued and in a plausible travel order, a *Conditions of Stay* box
  (*"The holder must dream in Somnian at all times. Fee 40 ZZZ, paid in
  dreams. No refunds in daylight."*), a *Dream Tax Paid* fee stamp, a
  sketch map of crescent-shaped Somnia, and a handwritten note:
  *"Do not wake the holder. — J."*
- **Boarding pass** — Somnia Air flight SM-014, Reverie → the Land of
  Nod, 19 JUN 2024, gate Dream 7, seat 14A. *"Have a pleasant dream."*

## Run it

```sh
python3 main.py            # writes out/entry.png
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` is Python 3.13 standard library only — no network, no
dependencies. It copies the rendered `entry.png` (1024×1024,
273,281 bytes, under the 1 MiB cap) to the output directory and verifies
the PNG signature, size, dimensions, and a byte-identical copy before
finishing. The output is deterministic: every run writes the same bytes.

The spread itself was drawn programmatically with Pillow
(see the build history in this repository's commit log); `entry.png` is
the rendered result committed beside the program.

## License

MIT — see [LICENSE](LICENSE).
