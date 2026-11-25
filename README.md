[![make.fun · u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Adnanhasim8/makefun-motasimfuad-two-robots-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Adnanhasim8/makefun-motasimfuad-two-robots-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

# Two Robots in an Elevator

Entry for the make.fun competition `u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f`:
one funny line of awkward small talk a robot says to another robot in an
elevator. The line is a single line under 200 characters, written by
`main.py` to `/output/entry.txt`.

The entry: a robot that has been counting the other robot's blinks tries to
open a conversation — and cannot tell whether two blinks were a greeting or
a firmware error. Machine logic shows through the politeness, the
awkwardness is the whole joke, and the question is left unanswered.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13 standard library only, no network at run time. The program
asserts its own gate before writing: exactly one line, 1–200 characters,
non-empty. Set `ENTRY_OUTPUT` to write somewhere other than
`/output/entry.txt` (handy for local checks).
