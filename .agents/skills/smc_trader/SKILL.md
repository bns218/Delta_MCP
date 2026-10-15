---
name: smc-trader
description: >-
  Provides the agent with the ability to autonomously scan for Smart Money Concepts (SMC) 
  setups like Fair Value Gaps (FVG) and execute them as paper trades on Delta Exchange via MCP.
---

# SMC & ICT Autonomous Trader Skill (Hardened Institutional Guardrails & Self-Learning)

This skill allows the agent to autonomously analyze live market data and execute Smart Money Concepts (SMC) trades on Delta Exchange with institutional risk guardrails, continuous learning memory, and dynamic hyperparameter optimization.

## Core Strategy & Timeframe Hierarchy

1.  **Timeframe Hierarchy (Strict Rule):**
    *   **Macro Bias & Order Blocks:** 1-Hour (1h) candles.
    *   **Market Structure Shift (MSS/CHoCH) & Confirmation:** 15-Minute (15m) candles. **MANDATORY**: No trade may be executed without a full 15-minute candle close confirmation.
    *   **Execution Tuning Only:** 5-Minute (5m) candles for discount entry / FVG refinement.
    *   *STRICT PROHIBITION:* 1-minute and 3-minute candles are strictly prohibited for structural reversal entries. They are noise during high-volume sessions.

2.  **Killzones (IST Time):**
    *   London Session: 12:30 PM - 3:30 PM IST (07:00 - 10:00 UTC)
    *   New York Session: 6:30 PM - 9:30 PM IST (13:00 - 16:00 UTC)
    *   *Rule:* Do not place trades outside of these high-volume killzones.

3.  **Terminal Liquidity Protection (Zero Front-Running Rule):**
    *   If a major unmitigated 24-hour liquidity pool (e.g. daily high, daily low, Asian high/low) is within 250 points of current price, **DO NOT ENTER COUNTER-TREND TRADES**.
    *   Wait for price to cleanly sweep the terminal liquidity pool FIRST.
    *   Wait for the 15-minute candle to close back inside the range (confirming an ICT Turtle Soup / SFP).
    *   If the 15-minute candle closes with body expansion beyond the level, **STAND ASIDE** as the trend is expanding.

4.  **Full Candle Acceptance Rule (No Wicking / No Premature Triggers):**
    *   Never enter on an active, open candle ("wick touch").
    *   Always wait for the 15-minute candle to CLOSE before generating an order signal.

## Execution Guardrails (Delta Exchange MCP)

1.  **Risk & Capital Cap:** Maximum $10.00 USD margin allocation per trade at 200x isolated leverage (24 contracts = 0.024 BTC).
2.  **Minimum Risk-to-Reward:** Strictly $\ge 1:2.5$.
3.  **Bracket Protection:** Every order MUST have a hard Stop Loss and Take Profit attached upon placement (`place_order` with bracket parameters or `place_bracket_order`).

## Dynamic ATR-Based Buffers & Multi-Tier TP Scaling

1.  **Dynamic ATR Stop Loss Buffer:**
    *   Base stop distance is anchored to the structural swing invalidation level + ATR buffer.
    *   Buffer formula: $\text{SL Buffer} = \max(50.0, 0.35 \times \text{ATR}_{15m})$.
    *   During high volatility (ATR > 200 pts), minimum stop buffer expands to 75.0 points to absorb liquidity wicks without invalidating structural thesis.
2.  **Dynamic Take Profit Scaling:**
    *   **TP1 (1:2.0 RR):** Secure 50% position profit; immediately advance hard Stop Loss to Entry (Breakeven).
    *   **TP2 (1:4.0 RR):** Secure 30% position profit; trail hard Stop Loss to the most recent 15m confirmed swing structural low/high.
    *   **TP3 (1:8.0 RR / Terminal Pool):** Let remaining 20% runner ride to major opposing 24-hour BSL/SSL pool.

## Institutional Memory & Playbook Signatures (`trade_memory.json`)

1.  **A+ Win Signature (Playbook Archetype #1):**
    *   *Setup:* 15m MSS + unmitigated London/NY FVG + Deep Discount (>50% Fib) + Unmitigated resting BSL pool.
    *   *Validation:* Confirmed by 15m body close. Resulted in Trade #1 (+914.5 pts / +$21.95 USD / 7.1 RR).
2.  **Failure Signature (Anti-Pattern Archetype #1):**
    *   *Hazard:* Micro-timeframe (<15m) premature entry while higher-timeframe sell displacement is actively seeking resting terminal liquidity (e.g. Trades #3 and #4 into $80,240/$80,062 SSL).
    *   *Remedy:* Block all counter-trend entries within 250 points of terminal liquidity until sweep + 15m SFP close is printed.

## Self-Healing Supervisor & Automated Circuit Breakers

1.  **2-Loss Session Cooldown Freeze:**
    *   If 2 trades hit Stop Loss within the same Killzone session, trigger an immediate **45-minute trading freeze**.
    *   During freeze, all new incoming entry signals are rejected. No order placement is permitted.
2.  **Daily Drawdown Hard Lock:**
    *   If cumulative daily loss reaches 5% ($10.00 USD), order placement is hard-locked until the next UTC 00:00 rollover.
3.  **Dynamic Frame Lockdown (Anti-Micro Trap):**
    *   Sub-15m confirmations (1m/3m) are strictly forbidden. Entry confirmation requires a full 15-minute candle close confirming MSS/CHoCH.
4.  **Continuous Self-Learning Loop:**
    *   After every closed position, the SMC Self-Learning subagent ingests the execution log into `trade_memory.json`, recalculates empirical win rates and expectancy, and refines ATR hyperparameters.
