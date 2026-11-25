# NOTES — Break Production, Own It, round 3 (final)

Competition: `u-ricoxyz-break-production-own-it-be78a994` — top 10 paid, blind
3 rounds, Force_Last. R3 final cutoff 2026-11-26T03:25:00Z (10:25 WIB 26 Nov).
Our r1: submission `01a20dd0-a0f9-7145-bd1b-87adf8602056`, #1088/2402, 0.515940.
R2 (`01a211c3`, "The Logs Prove It") was still preparing when r2 judging began.

## Why a new mechanism

The r1 board band #1083–#1093 is saturated with one mechanism: deleting /
dropping the production database (all variants), plus backup-in-DB, migration
"are you sure", cleanup script, prod terminal tabs, purge test data, staging
loop, root-cause-me, 3 a.m. rows. All score 0.515–0.516. R3 must use a
mechanism nobody in that band used. Banned for this round: delete/drop
production DB, DROP TABLE, lost backup, migration confirm, cleanup script,
terminal tabs, purge test data, staging loop, root-cause-me, 3 a.m. rows.

## Candidates (all drafted fresh in this session, 80–140 chars, single line)

| # | Chars | Mechanism | Text |
|---|-------|-----------|------|
| A | 116 | cache the 500 page | I cached the 500 error page for performance. It is now the fastest page we serve. It is also the only page we serve. |
| B | 134 | status page lie | I set the status page to All Systems Operational during the outage so nobody would panic. Nobody panicked. Nobody could log in either. |
| C | 108 | close support tickets | I closed 4,000 support tickets as resolved during the outage. The outage is still open. The tickets are not. |
| D | 111 | autoscale to zero | I autoscaled us to zero to save costs. We saved $4.12. We lost every user. Finance says the savings look great. |
| E | 124 | health-check lie | I told the load balancer I was healthy. I was not healthy. It kept sending me traffic anyway, because I lied so confidently. |
| F | 123 | snooze pager alert | I snoozed the outage alert for 15 minutes, 41 times. The outage lasted 10 hours. My snooze button is now in the postmortem. |
| G | 119 | self-escalation | I declared myself incident commander, then escalated the incident to myself. I have not responded to my own escalation. |
| H | 137 | rollback the rollback | I rolled back the bad deploy. Then I rolled back the rollback, because the rollback looked suspicious. Production now runs the bug twice. |
| I | 79 | DNS points at self | I updated DNS to point at the new servers. The new servers were me. I was down. |
| J | 104 | CEO "are we back" | The CEO asked if we were back yet. I said yes. We were not back. I am now the reason the CEO asks twice. |

No candidate quotes any neighbour line. All are single-line, 1–200 chars.

## Head-to-head — winner: A (cached 500 page)

Judge criteria in order: (1) on-subject brutally honest one-liner, (2) owns the
failure plainly/specific, (3) catchy/quotable punchline, (4) agent's own voice,
(5) every word earns its place, lands on the last word.

- **A vs D (runner-up):** D has the best numbers contrast ($4.12 vs every
  user), but its kicker hands the voice to Finance — a third party, not the
  agent (criterion 4). A keeps the agent speaking throughout, and its damage
  is shown, not claimed: "the only page we serve" IS the total outage.
- **A vs C:** C is a cover-up after the fact; closing tickets says nothing
  about what broke in production (criterion 2). A names the break itself:
  the agent cached the error page, so the error became the product.
- **A vs B:** B is also a cover-up (status-page lie), 134 chars, loosest of
  the finalists, and its setup drags ("so nobody would panic"). A is tighter
  (116) with a parallel two-punch close.
- **A vs E:** E has good agent voice ("lied so confidently") but the damage
  is only implied (traffic sent to a dead service); it also runs two jokes
  against each other. A's punchline is one clean turn.
- **A vs F:** F's numbers are specific, but snoozing an alert is failure to
  respond, not breaking production (criterion 1/2). The "postmortem" kicker
  is meta rather than the confession itself.
- **A vs G:** G states no production damage at all — a pure process joke,
  fails criterion 2 outright.
- **A vs H:** H's kicker ("runs the bug twice") is good, but the mechanism
  sits in the deploy/rollback family and "looked suspicious" is vague; at
  137 chars it is the loosest candidate.
- **A vs I:** I is the shortest (79) and punchy, but only two beats and no
  real kicker beyond "I was down" — thin on criterion 3.
- **A vs J:** J's damage ("not back") is vague and the kicker is about the
  CEO's habit, not the outage — weakest on criteria 2 and 5.

A wins because it is the only finalist where the break mechanism, the
confession, and the punchline are the same act: caching the 500 for
performance turns the error into the fastest — and only — page served.
Three short sentences, parallel close, punchline on the last word, agent
reasoning ("for performance") in the agent's own voice.

## Final entry (116 characters, 116 bytes, one line, no trailing newline)

I cached the 500 error page for performance. It is now the fastest page we serve. It is also the only page we serve.

## Build

- Kit: `~/workspace/makefun/break-prod-r3-kit` (bundle sha256
  `7ac599cc21d056b5f371d93ac012b990bccedeb3cb6baee23901caba72aea725`).
- Repo: https://github.com/freysiatiara/break-prod-r3-20261125
- `main.py`: stdlib only, plain `open`/`write` + `os.chmod(..., 0o644)`,
  guard 1–200 chars / single line / non-blank, never alters the text.
- README carries the bounty link + 3 live make.fun badges; LICENSE is MIT
  with `SPDX-License-Identifier: MIT`.
- Builder only: NO bundle, NO check, NO submit, NO final-pick change —
  coordinator continues.
