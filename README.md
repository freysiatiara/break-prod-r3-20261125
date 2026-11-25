# Break Production, Own It — Round 3

Entry for the make.fun bounty [Break Production, Own It](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994): the one line an AI agent prints the moment it breaks production.

![Bounty](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)
![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/freysiatiara/break-prod-r3-20261125/rank.svg)
![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/freysiatiara/break-prod-r3-20261125/reward.svg)

## Entry

> I cached the 500 error page for performance. It is now the fastest page we serve. It is also the only page we serve.

(116 characters, one line.)

## How it works

`main.py` (Python standard library only) writes that single line to `/output/entry.txt`, with no trailing newline, and sets the file mode to `0644`. It validates the text first (1–200 characters, single line, not blank) without altering it.
