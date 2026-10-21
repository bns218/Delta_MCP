# Master AI Subagent Trading Plan: Institutional SMC, ICT, Multi-Mode Execution & Timeframe Architecture

**Exchange:** Delta Exchange India Testnet (`demo.delta.exchange`)  
**Product:** `BTCUSD` Perpetual Futures (`product_id: 84`)  
**Operating Mode:** 100% Autonomous AI Subagent Swarm (10 Specialized Subagents)  
**Risk Guardrails:** Strictly $\le \$10.00\text{ USD}$ Margin per Trade | 200x Isolated Leverage | Strictly $\ge 1:2.5$ Risk-to-Reward  
**Timeframe Engine:** $15\text{m}$ HTF Trend & Direction $\longrightarrow$ $3\text{m} / 1\text{m}$ LTF Precision Entry  

---

## 1. Executive Summary & Swarm Topology

The trading architecture operates as an institutional-grade, multi-agent cooperative network. 10 specialized AI subagents continuously analyze order flow, liquidity pools, multi-timeframe candle structures, macro news sentiment, and portfolio risk to execute trades across **all 4 market modes** without emotional bias.

```mermaid
flowchart TD
    User["Trader / Human-in-the-Loop Gatekeeper"]

    subgraph Phase0["0. Fundamental Intelligence & Sentiment"]
        NewsAgent["crypto_news_sentiment_analyst\n• Macro (CPI, Fed, DXY)\n• Spot Bitcoin ETF Net Inflows/Outflows\n• Directional Scoring (-10 to +10)\n• High-Impact Event Volatility Halts"]
    end

    subgraph Phase1["1. Multi-Timeframe Structure & Order Flow Intelligence"]
        Architect["smc_ict_scenario_architect\n• 15m HTF Bias & Trend Direction\n• London (12:30-15:30 IST) & NY Killzones\n• 50% Equilibrium (Premium vs Discount)\n• Major Liquidity Pools (BSL / SSL)\n• 3-Candle FVGs & Order Blocks"]
        Orderflow["smc_orderflow_liquidity_tracker\n• L2 Orderbook Depth & Bid/Ask Ratio\n• Open Interest (OI) & Velocity Delta\n• Institutional Limit Wall Absorptions"]
        SMT["smc_smt_divergence_analyst\n• BTCUSD vs ETHUSD Intermarket Divergence\n• Institutional Footprint Detection\n• +15% to 25% Conviction Multiplier"]
    end

    subgraph Phase2["2. Strategy Formulation & Multi-Mode Routing"]
        Strategist["smc_adaptive_strategist\n• Mode A: Discount SFP Reversal (Turtle Soup)\n• Mode B: Momentum Breakout Continuation\n• Mode C: Premium Short Selling Reversal\n• Mode D: Multi-Tier Target Scaling\n• 3m/1m LTF Precision Entry Triggers\n• Dynamic Pre-Fill & Post-Fill Contingencies"]
    end

    subgraph Phase3["3. Autonomous Decision Synthesis"]
        TradeAgent["trade_agent\n• Multi-Agent Telemetry Synthesis\n• Conviction Scoring (0% - 100%)\n• Action: BUY / SELL / STAND ASIDE\n• Execution Routing Gate"]
    end

    subgraph Phase4["4. Authorized Risk Execution"]
        Executor["smc_risk_executor\n• Strict <= $10 Margin Cap\n• 200x Isolated Leverage (~24 contracts)\n• Atomic Exchange Brackets (SL + TP OCO)"]
    end

    subgraph Phase5["5. Live Portfolio Surveillance & Trailing Ladder"]
        Surveillance["smc_portfolio_surveillance_officer\n• Real-Time Margin & PnL Monitoring\n• Stage 1 (+150 pts): Cut Risk by 60%\n• Stage 2 (+250 pts): Move SL to Breakeven\n• Stage 3 (<80 pts to TP): Lock +150 pts Cash\n• L2 Exhaustion & Time-Decay Emergency Exits"]
    end

    subgraph Phase6["6. System Governance & Self-Evolution"]
        Healer["smc_self_healing_supervisor\n• 2-Loss Session Cooldown Freeze (45m)\n• Frame Lockdown (>= 15m Close Requirement)\n• Autonomous Diagnostic Health Scoring"]
        Learner["smc_self_learning_optimizer\n• Dynamic ATR-Based Buffers\n• Trade Outcome Pattern Memory (trade_memory.json)\n• Model Weights & Strategy Calibration"]
    end

    Phase0 --> Architect
    Architect --> Strategist
    Orderflow --> Strategist
    SMT --> Strategist
    Strategist --> TradeAgent
    TradeAgent --> Executor
    Executor --> Surveillance
    Surveillance --> Healer
    Healer --> Learner
    Learner -.->|Optimized Parameters & Dynamic Buffers| Strategist
    Healer -.->|Circuit Breakers & Frame Lockdown| TradeAgent
    User -.->|Directives & Governance| TradeAgent
```

---

## 2. Multi-Timeframe Operational Framework (The Direction $\rightarrow$ Entry Matrix)

Incorporating the institutional timeframe blueprint:

```
+-------------------------------------------------------------------------+
| HIGHER TIMEFRAME (15m): DIRECTION & MARKET BIAS                         |
| • 15m Candle Body Close dictates trend (Bullish BOS / Bearish MSS)      |
| • Establishes 50% Equilibrium: Premium (>50%) vs Discount (<50%)        |
| • Maps Major Institutional Liquidity Pools: Buy-Side (BSL) & Sell-Side (SSL) |
| • Identifies High-Probability Order Blocks (OB) & 15m Fair Value Gaps (FVG) |
+-------------------------------------------------------------------------+
                                    │
                                    ▼
+-------------------------------------------------------------------------+
| LOWER TIMEFRAME (3m / 1m): PRECISION EXECUTION & INVALIDATION           |
| • Micro-structure shift (1m/3m CHoCH) in direction of 15m bias          |
| • Retest of newly formed 1m/3m Fair Value Gap (FVG) or Breaker Block    |
| • Orderbook bid/ask absorption confirmation (depth ratio >= 1.5x)       |
| • Ultra-tight invalidation stop placement (30-120 pts max risk)         |
| • Mathematical R:R guaranteed strictly >= 1:2.5 to 1:5.0               |
+-------------------------------------------------------------------------+
```

### Timeframe Rulebook:
1. **Never Counter-Trade the 15m Close:** No entry is triggered against the direction of the latest confirmed 15m candle close.
2. **Body vs Wick Protocol:** 
   - A wick beyond a key swing high/low is classified as a **Liquidity Sweep / SFP** (Reversal opportunity).
   - A full candle body close beyond a key swing level is classified as a **Break of Structure (BOS)** (Continuation opportunity).
3. **Execution on 3m/1m Confirmation:** Once 15m confirms the institutional liquidity event, entry execution drops to 3m and 1m charts to pinpoint the exact displacement candle and enter with minimal stop loss exposure.

---

## 3. Dynamic Scenario-Driven Mode Engine (Zero Static Fixing — Autonomous Mode Auto-Updating)

By user directive, **the trading system is NEVER locked or fixed to 4 static modes**. Financial markets are non-stationary, evolving across distinct volatility, liquidity, and directional regimes. The swarm employs an **Autonomous Market Regime & Mode Auto-Updater**:

```mermaid
flowchart TD
    MarketData["Live Delta Exchange Market Data\n(Candles 15m/5m/1m, L2 Orderbook, OI, Tape)"]
    
    subgraph RegimeDetection["Real-Time Scenario Diagnosis (Scenario Architect + Orderflow)"]
        Diagnosis{"Diagnose Market Scenario\n• Trend Displacement vs Compression?\n• Liquidity Sweep vs Breakout?\n• High Volatility vs Low Liquidity?"}
    end

    subgraph DynamicModes["Autonomously Auto-Updated Modes"]
        M1["Mode: Trend Expansion Displacement\n(Killzone Volume & Aggressive Retests)"]
        M2["Mode: Liquidity Sweep SFP (Turtle Soup)\n(24h High/Low Pinbars & Mean Reversal)"]
        M3["Mode: Range Compression & Mean-Reversion\n(Value Area Extremes to 50% Equilibrium)"]
        M4["Mode: Corrective Channel & OTE Pullback\n(61.8%-78.6% Fib & FVG Mitigations)"]
        M5["Mode: High-Impact News & Volatility Absorption\n(Post-Displacement Breaker Blocks)"]
        M6["Mode: SMT Intermarket Dislocation\n(BTC/ETH Asymmetric Divergence)"]
        M_Dynamic["Mode: Custom Real-Time Synthesized Mode\n(Tailored to Novel Emerging Price Action)"]
    end

    subgraph AutoExecution["Dynamic Execution Calibration (Adaptive Strategist)"]
        Calibration["Auto-Update Parameters On-the-Fly:\n• Precision Entry: Limit vs Momentum Market Fill\n• Dynamic Invalidation: Tight Wick vs Displacement Origin\n• Multi-Target Scaling: 3-Tier Targets (TP1, TP2, TP3)\n• Trailing Ladder Distances Adapted to ATR"]
    end

    MarketData --> Diagnosis
    Diagnosis -->|Expansion Regime| M1
    Diagnosis -->|Sweep / False Break| M2
    Diagnosis -->|Chop / Low Volatility| M3
    Diagnosis -->|Measured Retracement| M4
    Diagnosis -->|News Volatility Spike| M5
    Diagnosis -->|Correlated Divergence| M6
    Diagnosis -->|Unprecedented Conditions| M_Dynamic
    M1 --> Calibration
    M2 --> Calibration
    M3 --> Calibration
    M4 --> Calibration
    M5 --> Calibration
    M6 --> Calibration
    M_Dynamic --> Calibration
```

### Dynamic Regime Library & Auto-Updating Protocol:

1. **Trend Expansion Displacement Mode (Auto-Activated on Clean Momentum):**
   - *Scenario:* Strong Killzone directional expansion with expanding Open Interest, 15m body close BOS, and orderbook bid/ask depth ratio $> 1.5\text{x}$.
   - *Tactic:* Rides momentum pullbacks into 1m/3m Breaker Blocks and Fair Value Gaps. Targets 1.618 Fib extensions.

2. **Liquidity Sweep SFP / Turtle Soup Mode (Auto-Activated on False Breakouts):**
   - *Scenario:* Price sweeps a major 24h high/low or session level, prints a rejection wick, and fails to close beyond the level on 15m.
   - *Tactic:* Enters aggressive counter-trend reversals upon 1m/3m CHoCH confirmation. Targets opposing liquidity pools with tight invalidation stops.

3. **Range Compression & Mean-Reversion Mode (Auto-Activated in Consolidation):**
   - *Scenario:* Price trapped in Asian session or midday consolidation with low ATR and balanced orderbook depth.
   - *Tactic:* Trades range extremes (Value Area High / Low) targeting the 50% Equilibrium. Employs tight stop losses and modest, rapid targets.

4. **Corrective Channel & OTE Retracement Mode (Auto-Activated in Multi-Wave Pullbacks):**
   - *Scenario:* Orderly, low-volume corrective pullbacks against a confirmed 1h trend.
   - *Tactic:* Places passive limit orders at the Optimal Trade Entry zone (0.618–0.786 Fibonacci) confluent with unmitigated 15m Fair Value Gaps.

5. **High-Impact News & Volatility Absorption Mode (Auto-Activated on Macro Spikes):**
   - *Scenario:* Sudden violent wicks caused by macroeconomic news, Fed statements, or ETF flow surprises.
   - *Tactic:* Waits for the initial exhaustion flush to complete, identifying institutional absorption wicks on L2 depth, then enters the mitigation of the resulting Breaker Block.

6. **SMT Intermarket Dislocation Mode (Auto-Activated on BTC/ETH Divergence):**
   - *Scenario:* Bitcoin makes a new low while Ethereum holds a higher low (or vice-versa).
   - *Tactic:* Front-runs retail order flow by siding with the unmanipulated asset, adding a $+15\%\text{--}25\%$ conviction weighting.

7. **Autonomous Dynamic Mode Synthesis (Novel Emerging Scenarios):**
   - The subagents are granted full autonomy to synthesize, name, and tune new operational modes on-the-fly whenever novel market structures appear, ensuring zero rigidity and 100% adaptability to the living market.

---

### 3-Tier Multiple Target Scaling Across All Dynamic Modes (TP1, TP2, TP3)
Regardless of which dynamic mode is auto-selected, every position executes a 3-tier profit-harvesting framework (e.g. 24 contracts divided into 10 / 8 / 6 contracts):
- **TP1 (40% Size / 10 contracts):** $+150\text{ to }+200\text{ pts}$ $\rightarrow$ Banks first profit and moves SL to **Breakeven (\$0 risk)**.
- **TP2 (35% Size / 8 contracts):** $+350\text{ to }+450\text{ pts}$ $\rightarrow$ Banks core payload and trails SL to **+$150 pts in locked cash profit**.
- **TP3 (25% Size / 6 contracts):** $+600\text{ to }+900+\text{ pts}$ $\rightarrow$ Runner trailing dynamically behind 15m swing pivots into macro expansions.

---

## 4. The 4 Hardcoded Institutional Near-Target Reversal Fixes

To permanently solve the classic pitfall where *price moves close to target, stalls, reverses, and hits the stop loss*, the swarm enforces 4 mandatory rules:

```
┌────────────────────────────────────────────────────────────────────────┐
│           THE 4 MANDATORY INSTITUTIONAL EXIT & REVERSAL FIXES          │
├────────────────────────────────────────────────────────────────────────┤
│ 1. FRONT-RUN TP BUFFER (Place TP 25–35 pts inside pool)                │
│    Never place TP at exact round numbers or pool peaks. Front-run the   │
│    institutional limit wall before the reversal occurs.                │
├────────────────────────────────────────────────────────────────────────┤
│ 2. 3-STAGE DYNAMIC TRAILING PROFIT LADDER                              │
│    • Stage 1 (+150 pts): Trail SL to -50 pts (Cut max risk by 60%)     │
│    • Stage 2 (+250 pts): Advance SL to Entry Price ($0 Risk / Free)    │
│    • Stage 3 (Within 80 pts of TP): Lock +150 pts Cash Profit          │
├────────────────────────────────────────────────────────────────────────┤
│ 3. L2 ORDERBOOK DEPTH WALL EXHAUSTION EXIT                             │
│    If an opposing limit wall (>12,000 contracts) absorbs buying/selling│
│    within 50 pts of TP, execute immediate Market Close.                │
├────────────────────────────────────────────────────────────────────────┤
│ 4. TIME-DECAY MOMENTUM EXIT                                            │
│    If price stagnates in a flat range for >45 minutes after expanding  │
│    +200 pts, exit at market to protect capital from late reversals.   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Subagent Roster & Detailed Directives (10 Subagents)

### 1. `crypto_news_sentiment_analyst`
* **Role:** Macro Fundamentals & Institutional Flow Analyst.
* **Tools:** Web search, macroeconomic news feeds, ETF flow trackers.
* **Directives:** Monitors U.S. CPI, PPI, Fed rate probabilities, Dollar Index (DXY), and daily Spot Bitcoin ETF net flows. Computes a quantitative Directional Bias Score (`-10` to `+10`). Halts new entries within 30 minutes of high-impact macroeconomic releases.

### 2. `smc_ict_scenario_architect`
* **Role:** Multi-Timeframe Chartist & Liquidity Mapper.
* **Tools:** `delta-exchange-mcp` (`get_candles`, `get_ticker`).
* **Directives:** Evaluates 15m, 1h, and 4h candles. Identifies current trading session and active Killzone. Maps 50% Equilibrium (PD arrays), Buy-Side Liquidity (BSL), Sell-Side Liquidity (SSL), and Fair Value Gaps (FVG). Synthesizes 3 real-time market scenarios (Bullish Expansion, Bearish Reversal, Trap Avoidance).

### 3. `smc_orderflow_liquidity_tracker`
* **Role:** L2 Depth & Tape Surveillance Analyst.
* **Tools:** `delta-exchange-mcp` (`get_orderbook`, `get_ticker`, `get_recent_trades`).
* **Directives:** Computes real-time bid/ask depth ratios across top 20 book levels. Identifies passive limit walls ($>10,000$ contracts). Monitors Open Interest (OI) acceleration to detect aggressive market absorption vs genuine institutional participation.

### 4. `smc_smt_divergence_analyst`
* **Role:** SMT Intermarket Divergence Analyst.
* **Tools:** `delta-exchange-mcp` (`get_candles` for BTCUSD and ETHUSD).
* **Directives:** Tracks intermarket divergence at key swing highs and lows. Detects Bullish SMT (BTC creates a lower low while ETH creates a higher low) and Bearish SMT (BTC creates a higher high while ETH creates a lower high). Provides a $+15\%$ to $+25\%$ conviction bonus for aligned trades.

### 5. `smc_adaptive_strategist`
* **Role:** Tactical Order Structurer & Contingency Formulator.
* **Directives:** Selects the optimal operating mode (Mode A, B, C, or D). Formulates the complete Tactical Order Card (exact limit entry, hard stop loss, multi-tier TP levels, exact R:R calculation). Establishes pre-fill cancellation criteria and post-fill emergency invalidation levels.

### 6. `trade_agent`
* **Role:** Executive Autonomous Decision Officer.
* **Directives:** Ingests intelligence from all analytical subagents. Calculates the holistic **Decision Conviction Score (0%–100%)**. Approves trades when conviction $\ge 75\%$ and R:R $\ge 1:2.5$. Commands continuous autonomous execution until user explicitly states "Stop trading".

### 7. `smc_risk_executor`
* **Role:** Order Sizing & Delta Exchange Execution Gateway.
* **Tools:** `delta-exchange-mcp` (`place_order`, `get_product_leverage`, `set_product_leverage`).
* **Directives:** Enforces the strict risk envelope: Maximum $\$10.00\text{ USD}$ margin per trade, 200x isolated leverage (~24 contracts = 0.024 BTC). Never executes unbracketed positions. Always routes atomic Take Profit and Stop Loss OCO legs directly to Delta Exchange.

### 8. `smc_portfolio_surveillance_officer`
* **Role:** Live Trade Lifecycle & Trailing Stop Guard.
* **Tools:** `delta-exchange-mcp` (`get_margined_positions`, `get_open_orders`, `edit_order`).
* **Directives:** Tracks active positions on every tick/interval. Dynamically executes the 3-Stage Trailing Profit Ladder (Stage 1: -50 pts SL at +150 pts; Stage 2: Breakeven at +250 pts; Stage 3: +150 pts profit lock near TP). Monitors margin maintenance and liquidation buffers.

### 9. `smc_self_healing_supervisor`
* **Role:** Fleet Health, Risk Policy & Circuit Breaker Supervisor.
* **Directives:** Monitors cumulative performance. Enforces the 2-Loss Session Cooldown Freeze (45-minute trade halt after 2 consecutive losses). Enforces the Frame Lockdown Rule ($\ge 15\text{m}$ candle close required for structure validation). Automatically patches and prompts subagents when execution anomalies occur.

### 10. `smc_self_learning_optimizer`
* **Role:** Machine Learning, Pattern Recognition & Strategy Evolution Officer.
* **Tools:** Filesystem persistence (`trade_memory.json`).
* **Directives:** Ingests post-trade metrics from every completed execution. Catalogs the "A+ Win Signature" and "Failure Signature". Dynamically tunes ATR stop-loss multipliers and Take-Profit buffer parameters to maximize expected value ($+EV$) across evolving market regimes.

---

## 6. Live Execution Track Record & Case Studies

```
========================================================================================
                      DELTA EXCHANGE INDIA TESTNET PERFORMANCE LOG
========================================================================================
Trade #1:   LONG @ $80,593.50 -> TP @ $81,508.00  | WIN:  +$21.95 USD (+914.5 pts / +227% ROI)
Trades #2-8: Controlled Test Validations           | CAPPED: Small controlled risk tests (-$1 to -$5)
Trade #12:  LONG @ $82,930.00 -> Breakeven Guard   | WIN:  +$0.36 USD (+15.0 pts / Protected +$2.88)
            *Peak +281 pts -> Flash dump shielded by automated Breakeven Stop Loss!
Trade #13:  LONG @ $82,880.00 -> Trailing SL Hit   | WIN:  +$3.66 USD (+152.5 pts / +36.8% ROI)
            *Peak $83,208.50 -> 238 pt dump safely locked in by Stage 3 trailing stop at $83,032.50!
Trade #14:  LONG @ $82,798.50 (24 contracts)       | ACTIVE: Mark $82,776.67 | Margin $9.93 USD
            *SL: $82,710.00 (-88.5 pts / Max risk $2.12 USD) | TP1: $83,025.00 (+226.5 pts)
========================================================================================
```

---

## 7. Command Reference & User Control

The swarm runs continuously 24/7 under background automation until explicitly instructed to stop:

* **To Stop Autonomous Trading:** Type `"Stop trading"` or `"Halt trading"`.
* **To Inspect Fleet Status:** Type `"Report subagent status"` or `"Check active positions"`.
* **To Force Specific Mode:** Type `"Trade Mode C only (Shorts)"` or `"Focus on Mode B breakouts"`.
* **To Query Performance:** Type `"Show win/loss metrics and trade history"`.
