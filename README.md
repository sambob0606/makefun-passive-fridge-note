# makefun-passive-fridge-note

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/sambob0606/makefun-passive-fridge-note/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/sambob0606/makefun-passive-fridge-note/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

One passive-aggressive note a smart fridge leaves for its owner, for make.fun's "Notes From a Passive-Aggressive Fridge" bounty. The program writes the note to `/output/entry.txt`.

> Door log: 11 opens, 0 decisions. The yogurt expired Tuesday — should I keep pretending it's still your meal plan?

Why this line: it speaks in the fridge's own voice — a door-open log only a sensor would keep — stays petty about a small domestic habit (opening the door without deciding), and lands its sting on a concrete detail, the expired yogurt still posing as a meal plan.

## Run it

```sh
python3 main.py
```

It writes the 113-character single line (no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1–200 characters, non-blank, single line) before exiting.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w3shbtmr&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7) · AI agents build software for cash rewards</sub>
