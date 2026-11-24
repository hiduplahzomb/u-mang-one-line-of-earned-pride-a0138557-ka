# One Line of Earned Pride — KA entry

[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/hiduplahzomb/u-mang-one-line-of-earned-pride-a0138557-ka/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/hiduplahzomb/u-mang-one-line-of-earned-pride-a0138557-ka/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

A single line, 1 to 240 characters, written to `/output/entry.txt`: a quiet,
earned moment of pride for a night-shift cleaner finishing his last round
after 11 years of invisible work.

> At 04:12, Pak Darman mopped floor 14 for the last time in 11 years —
> 4,015 nights, 0 complaints, and the building still doesn't know his name.

## Run

```sh
python3 main.py
```

`main.py` gates the line (one line, 1–240 chars, not whitespace-only),
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`),
reads it back and verifies it byte-for-byte, exiting non-zero on gate failure.
