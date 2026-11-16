# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/amber-meteor-15/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/amber-meteor-15/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4,072 bytes of Python (main.py): a 0x88 board with incremental make/unmake, alpha-beta search with iterative deepening under a fixed 30,000-node budget — fully deterministic, no clock and no randomness, so a replay plays the same moves — plus a quiescence search over captures and promotions that also searches every check evasion, MVV-LVA move ordering with the previous iteration's best move first, and a piece-square-table evaluation. It plays the tiny-chess-01 gauntlet through the env API: each turn it reads the served FEN, searches, and answers with its move in UCI.

## Run it

```sh
MAKEFUN_ENV_URL=http://store:8080 python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=2aet9t8w&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
