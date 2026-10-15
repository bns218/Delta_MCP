# SMC, ICT & Price Action Multi-Agent Trading System

Autonomous trading architecture for **Delta Exchange India** integrating Smart Money Concepts (SMC), Inner Circle Trader (ICT) principles, Classical Price Action, and real-time Macro/Crypto News Sentiment Analysis.

---

## 1. Quick Start

Run the full multi-agent pipeline:
```bash
python smc_trading_engine.py --mode scan
```

---

## 2. Integrated Subagents

| Subagent Module | Core Role |
| :--- | :--- |
| **`NewsSentimentEngine`** | Collects live macro catalysts (CPI, Fed, DXY) & ETF flows; scores directional bias (-10 to +10). |
| **`SMCStructureEngine`** | Connects to Delta Exchange; maps 1h & 5m market structure, Killzones, 50% Equilibrium, BSL/SSL pools, and FVGs. |
| **`AdaptiveStrategyEngine`** | Computes exact Limit Entry, Hard Stop Loss, Tiered Targets (TP1–TP3), and Dynamic Emergency Exit Triggers. |
| **`RiskExecutionEngine`** | Sizes position strictly within a $10 margin allocation (200x leverage) and validates R:R >= 1:2.5. |
| **`SurveillanceEngine`** | Monitors open orders, trails Stop Loss to Breakeven at TP1, and triggers emergency cuts on FVG Inversion. |

---

## 3. Session Killzones (IST)

* **London Open:** 12:30 PM – 3:30 PM IST (07:00 – 10:00 UTC)
* **New York Open:** 6:30 PM – 9:30 PM IST (13:00 – 16:00 UTC)
* *Rule:* Outside these windows, the engine operates in Accumulation/Surveillance mode and waits for institutional volume.
