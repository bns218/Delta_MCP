---
name: smc-trader
description: >-
  Provides the agent and subagent fleet with the full institutional framework for Smart Money Concepts (SMC),
  Inner Circle Trader (ICT), Price Action, Order Flow Depth, and SMT Divergence trading on Delta Exchange India.
---

# Institutional SMC, ICT & Price Action Trading Desk (10-Subagent Architecture)

This master skill governs the autonomous market scanning, structural mapping, tactical strategy formulation, decision synthesis, and execution on Delta Exchange India (`BTCUSD` perpetual).

---

## 🏛️ 10-Subagent Multi-Agent Swarm

The trading desk operates as an interconnected AI hierarchy:
1. **Crypto News Sentiment Analyst:** Real-time macro drivers, DXY, interest rates, and institutional spot ETF flows (-10 to +10 score).
2. **SMC/ICT Scenario Architect:** Higher Timeframe (1h/15m) bias, Market Structure Shifts (MSS/CHoCH), FVGs, Order Blocks, and Liquidity Pools (BSL/SSL).
3. **Order Flow & Liquidity Depth Analyst:** Level-2 orderbook depth ratio, bid/ask imbalances, passive resting absorption walls, and Open Interest velocity.
4. **SMT Intermarket Divergence Analyst:** Cross-asset correlation (BTCUSD vs ETHUSD) detecting institutional accumulation/distribution divergences.
5. **Tactical Strategy & Contingency Officer:** Precise limit entries, hard stops, tiered TP scaling ($\ge 1:2.5$ R:R), and pre/post-fill invalidation shields.
6. **Trade Agent (Autonomous Decision Officer):** Independent synthesis of multi-agent telemetry, quantitative conviction scoring (0%–100%), and trade stance formulation (BUY, SELL, STAND ASIDE).
7. **Risk & Execution Officer:** Delta Exchange MCP gateway with strict capital preservation ($\le \$10.00\text{ USD}$ margin, 200x isolated leverage, atomic brackets).
8. **Portfolio Surveillance Officer:** Live trade monitoring, automated Breakeven stop advance (+250 pts / TP1), trailing structural locks, and liquidation buffer enforcement.
9. **Self-Healing Supervisor:** Autonomous circuit breakers, 2-loss 45-minute cooldown freeze, $\ge 15\text{m}$ frame lockdown, and subagent auto-patching.
10. **Self-Learning Optimizer:** Dynamic ATR buffer calibration, empirical win/loss pattern bank, and continuous updates to `trade_memory.json`.

---

## 🧭 Core Strategy & Timeframe Hierarchy

1. **Timeframe Hierarchy:**
   - **Macro Bias & Swing Highs/Lows:** 1-Hour (1h) candles.
   - **Structure Shifts & Entry Confirmation:** 15-Minute (15m) candles. **MANDATORY**: No trade signal is valid without a confirmed 15m candle body close.
   - **Execution Refinement:** 5-Minute (5m) candles for FVG midpoint (CE) refinement.
   - *Strict Prohibition:* 1m and 3m candles are strictly prohibited for reversal confirmation.

2. **Killzones (IST Time):**
   - **London Session:** 12:30 PM – 3:30 PM IST (07:00 – 10:00 UTC)
   - **New York Session:** 6:30 PM – 9:30 PM IST (13:00 – 16:00 UTC)
   - *Rule:* Avoid aggressive breakout entries outside of primary killzones unless orderbook depth and volume confirm displacement.

3. **Terminal Liquidity Protection (Zero Front-Running Rule):**
   - If a major unmitigated 24-hour liquidity pool (Daily High, Daily Low, Asian High/Low) is within 250 points of current price, **DO NOT ENTER COUNTER-TREND TRADES**.
   - Wait for price to cleanly sweep the liquidity pool FIRST.
   - Wait for the 15-minute candle to close back inside the range (confirming ICT Turtle Soup / Swing Failure Pattern).
   - If the candle body closes through the level, **STAND ASIDE** as the trend is expanding.

4. **Candle Acceptance Rule:**
   - Never enter on an active, unfinished candle ("wick touch").
   - Always await the 15-minute candle CLOSE before generating an order trigger.

---

## ⚖️ Autonomous Decision Matrix & Conviction Scoring

The **Trade Agent** computes an institutional Conviction Score ($0\% \text{ to } 100\%$):
- **Base Structure & FVG (Scenario Architect):** +30%
- **Macro News & ETF Net Inflows (Sentiment Analyst):** +20%
- **Orderbook Depth & Bid/Ask Dominance (Order Flow):** +15%
- **SMT Intermarket Divergence Confirmation (SMT Analyst):** +15%
- **Tactical R:R $\ge 1:2.5$ & Clean Invalidation (Adaptive Strategist):** +20%

**Decision Thresholds:**
- **Conviction $\ge 80\%$:** Formulate Trade Proposal (BUY / SELL) and present to User for Rule #0 Authorization.
- **Conviction $< 80\%$:** Formulate Autonomous Decision: **STAND ASIDE**.

---

## 🛡️ Risk Rules & Delta Exchange MCP Execution

0. **Rule #0 — Human-in-the-Loop Confirmation (STRICT & UNBREAKABLE):**
   - **NO live order** (market, limit, or bracket) may ever be dispatched to Delta Exchange without direct, explicit, written user approval (e.g. "Execute", "Approve", "Place order").
   - Status inquiries (e.g. "are you trading", "start trading", "what is status") are informational prompts that trigger multi-agent scanning and analysis, NOT automated order execution.
1. **Risk Cap:** Strictly $\le \$10.00\text{ USD}$ margin per position at 200x isolated leverage (~24 contracts = 0.024 BTC).
2. **Minimum R:R:** Strictly $\ge 1:2.5$.
3. **Atomic Bracket Protection:** All orders must be placed with native stop loss and take profit attached via `delta-exchange-mcp`.
4. **Automated Breakeven Trailing:** Once price reaches +250 points or hits TP1, the Portfolio Surveillance Officer advances Stop Loss to entry price (Breakeven).

---

## 🧠 Institutional Memory & Playbook Signatures (`trade_memory.json`)

- **A+ Win Archetype:** 15m MSS + unmitigated London/NY FVG + Deep Discount (>50% Fib) + Unmitigated resting BSL pool.
- **Failure Anti-Pattern:** Premature micro-timeframe (<15m) counter-trend entries into active institutional displacement seeking terminal resting liquidity.
- **Dynamic ATR Buffer:** $\text{SL Buffer} = \max(50.0, 0.35 \times \text{ATR}_{15m})$.
