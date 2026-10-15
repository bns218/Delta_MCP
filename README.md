# Institutional SMC, ICT & Price Action Multi-Agent Trading System

[![Status: Production-Grade](https://img.shields.io/badge/Status-Operational-brightgreen.svg)]()
[![Exchange: Delta Exchange](https://img.shields.io/badge/Exchange-Delta%20Exchange%20India-blue.svg)]()
[![Model Context Protocol: Enabled](https://img.shields.io/badge/MCP-delta--exchange--mcp-orange.svg)]()
[![Architecture: 6--Subagent Fleet](https://img.shields.io/badge/Architecture-Autonomous%20Subagents-purple.svg)]()
[![Risk: Strict Max Margin Cap](https://img.shields.io/badge/Risk-Max%20$10%20Margin%20Cap-red.svg)]()

Autonomous, institutional-grade algorithmic trading architecture built for **Delta Exchange India** (`BTCUSD` perpetual). The system fuses **Smart Money Concepts (SMC)**, **Inner Circle Trader (ICT)** methodologies, **Classical Price Action**, and **Real-Time Macro & Crypto Sentiment Analysis** into a coordinated multi-agent hierarchy with closed-loop **Self-Healing** and **Self-Learning** capabilities.

---

## 🏛️ System Architecture

The system operates strictly via specialized AI subagents communicating over the Model Context Protocol (MCP) through `delta-exchange-mcp`:

```
                           ┌─────────────────────────────────────────┐
                           │   Crypto News & Sentiment Analyst       │
                           │   • Macro Catalysts (Fed, CPI, DXY)     │
                           │   • Spot ETF Net Flows & Social Alpha   │
                           │   • Directional Bias Score (-10 to +10) │
                           └────────────────────┬────────────────────┘
                                                │
                                                ▼
                           ┌─────────────────────────────────────────┐
                           │      SMC/ICT Scenario Architect         │
                           │   • Market Structure Shift (MSS / CHoCH)│
                           │   • Fair Value Gaps (FVG) & OBs         │
                           │   • Liquidity Pools (BSL/SSL Sweeps)    │
                           │   • ICT Killzones (London/NY Opens)     │
                           └────────────────────┬────────────────────┘
                                                │
                                                ▼
                           ┌─────────────────────────────────────────┐
                           │   Tactical Strategy & Contingency       │
                           │   • Limit Order Placement & R:R >= 1:2.5│
                           │   • Pre-Fill Invalidation Shields       │
                           │   • Tiered Profit Scaling (TP1, 2, 3)   │
                           │   • Dynamic FVG Inversion Emergency Cuts│
                           └────────────────────┬────────────────────┘
                                                │
                                                ▼
                           ┌─────────────────────────────────────────┐
                           │       Risk & Execution Officer          │
                           │   • Strict <= $10 Margin Cap            │
                           │   • 200x Isolated Leverage              │
                           │   • Atomic Bracket Orders (SL + TP OCO) │
                           └────────────────────┬────────────────────┘
                                                │
                   ┌────────────────────────────┴────────────────────────────┐
                   ▼                                                         ▼
┌───────────────────────────────────────┐         ┌───────────────────────────────────────┐
│     Self-Healing Supervisor           │         │      Self-Learning Optimizer          │
│  • Micro-Timeframe Trap Shield        │         │  • Dynamic ATR-Based Stop Buffers     │
│  • 2-Loss Session Cooldown Freeze     │         │  • A+ Win vs Failure Pattern Memory   │
│  • Terminal Pool Liquidity Protection │         │  • Market Regime Classification       │
│  • Autonomous Subagent Auto-Patching  │         │  • Persistent Trade Memory (`.json`)  │
└───────────────────────────────────────┘         └───────────────────────────────────────┘
```

---

## 🤖 Specialized Subagent Fleet

1. **[`Crypto News Sentiment Analyst`](.agents/agents/crypto_news_sentiment_analyst/agent.md)**
   - Gathers live global macro data (US CPI, Federal Reserve policy, DXY) and institutional spot ETF inflows/outflows.
   - Computes a quantitative Directional Bias Score (-10 to +10) and Event Risk rating (LOW, MEDIUM, HIGH, CRITICAL).

2. **[`SMC/ICT Scenario Architect`](.agents/agents/smc_ict_scenario_architect/agent.md)**
   - Anchors exclusively to $\ge 15\text{m}$ timeframes for institutional structural clarity.
   - Maps 50% Equilibrium (Discount vs Premium), unmitigated Fair Value Gaps (FVGs), Breaker Blocks, and Buy-Side/Sell-Side Liquidity pools.

3. **[`Tactical Strategy & Contingency Officer`](.agents/agents/smc_adaptive_strategist/agent.md)**
   - Synthesizes tactical execution cards with strict $R:R \ge 1:2.5$.
   - Enforces pre-fill invalidations (e.g. cancels resting limit orders if the profit target is front-run prior to entry).

4. **[`Risk & Execution Officer`](.agents/agents/smc_risk_executor/agent.md)**
   - Manages live order execution on Delta Exchange India testnet.
   - Enforces strict capital preservation: $\le \$10.00\text{ USD}$ margin per trade at 200x leverage.
   - Implements native bracket orders with automatic OCO (One-Cancels-the-Other) protective stops.

5. **[`Self-Healing Supervisor`](.agents/agents/smc_self_healing_supervisor/agent.md)**
   - Monitors session health and detects behavioral anomalies (e.g. over-trading, counter-trend execution).
   - Enforces a mandatory **2-Loss 45-Minute Session Cooldown Freeze** and shields entries near unmitigated 24-hour extremes.

6. **[`Self-Learning Optimizer`](.agents/agents/smc_self_learning_optimizer/agent.md)**
   - Ingests settled trade data and updates [`trade_memory.json`](trade_memory.json).
   - Calibrates dynamic ATR buffers, trailing stop mechanics, and regime-based position sizing.

---

## 📊 Live Terminal Dashboard

The project includes an interactive, dark-mode terminal UI [`smc_dashboard.html`](smc_dashboard.html) featuring:
- Real-time account equity & profit tracking
- Multi-agent live status and system health scores
- Active order cards, execution logs, and risk limits
- Interactive SMC market structure map (Equilibrium, BSL, SSL, Discount FVG)

---

## 📚 Knowledge Base & Artifacts

- **[SMC, ICT & Price Action Encyclopedia](smc_ict_price_action_encyclopedia.md):** Complete technical reference covering 50+ institutional concepts across structure, liquidity, ICT models, and candlestick psychology.
- **[Subagents Master Trading Plan](subagents_trading_plan.md):** Detailed technical specifications, agent protocols, and operational workflows.
- **[Institutional Trade Memory](trade_memory.json):** Documented institutional case files, win signatures, failure patterns, and adaptive parameters.

---

## ⚙️ Configuration & Delta Exchange MCP Setup

This system interfaces directly with Delta Exchange via the **Model Context Protocol (MCP)** server:

### Prerequisites
- Node.js & Python 3.10+
- Delta Exchange India Account & API Credentials (Testnet or Live)
- MCP client (e.g., Antigravity, Claude Desktop, Cursor, or VS Code)

### Environment Configuration
Configure your MCP settings with your Delta Exchange credentials:
```json
{
  "mcpServers": {
    "delta-exchange-mcp": {
      "command": "uvx",
      "args": ["delta-exchange-mcp@latest"],
      "env": {
        "DELTA_ENVIRONMENT": "india_testnet",
        "DELTA_API_KEY": "YOUR_API_KEY",
        "DELTA_API_SECRET": "YOUR_API_SECRET"
      }
    }
  }
}
```

---

## 🛡️ Risk Rules & Operational Guardrails

- **Maximum Allocation:** Strictly capped at $\le \$10.00\text{ USD}$ margin per position (~24 contracts = 0.024 BTC).
- **Minimum Risk-to-Reward:** Strictly $\ge 1:2.5$.
- **Timeframe Anchor:** Strictly $\ge 15\text{m}$ candle body close confirmation (sub-15m entries forbidden).
- **Terminal Pool Shield:** Zero counter-trend positions within 250 points of unmitigated 24-hour high/low liquidity pools.
- **Macro Volatility Circuit Breaker:** Complete order entry freeze whenever Macro Directional Bias Score is $\le -4.0$ or Event Severity is `CRITICAL`.

---

## 📜 License
MIT License. For educational, research, and algorithmic testing purposes.
