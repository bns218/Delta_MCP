import json

def identify_market_structure(candles):
    swing_highs = []
    swing_lows = []
    for i in range(2, len(candles) - 2):
        if candles[i]['high'] > candles[i-1]['high'] and candles[i]['high'] > candles[i-2]['high'] and \
           candles[i]['high'] > candles[i+1]['high'] and candles[i]['high'] > candles[i+2]['high']:
            swing_highs.append(candles[i])
        if candles[i]['low'] < candles[i-1]['low'] and candles[i]['low'] < candles[i-2]['low'] and \
           candles[i]['low'] < candles[i+1]['low'] and candles[i]['low'] < candles[i+2]['low']:
            swing_lows.append(candles[i])
    return swing_highs, swing_lows

def get_premium_discount(candles):
    if not candles: return 0, 0, 0
    highest = max(c['high'] for c in candles)
    lowest = min(c['low'] for c in candles)
    midline = lowest + ((highest - lowest) / 2)
    return highest, lowest, midline

def scan_advanced_smc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            start_idx = content.find('{')
            if start_idx != -1:
                data = json.loads(content[start_idx:])['result']
                data = sorted(data, key=lambda x: x['time'])
                
                if len(data) < 10:
                    print("Not enough data.")
                    return

                highest, lowest, midline = get_premium_discount(data)
                swing_highs, swing_lows = identify_market_structure(data)
                current_price = data[-1]['close']
                
                trend = "Ranging"
                if swing_highs and current_price > swing_highs[-1]['high']:
                    trend = "Bullish"
                elif swing_lows and current_price < swing_lows[-1]['low']:
                    trend = "Bearish"

                high_prob_bullish = []
                high_prob_bearish = []

                for i in range(len(data)-2):
                    c1, c2, c3 = data[i], data[i+1], data[i+2]
                    # Bearish
                    if c1['low'] > c3['high']:
                        if c3['high'] >= midline:
                            ob = c1['high'] if c1['close'] > c1['open'] else None
                            high_prob_bearish.append((c3['high'], c1['low'], ob))
                    # Bullish
                    elif c1['high'] < c3['low']:
                        if c3['low'] <= midline:
                            ob = c1['low'] if c1['close'] < c1['open'] else None
                            high_prob_bullish.append((c1['high'], c3['low'], ob))
                
                print("=========================================")
                print("       AI PRE-TRADE STRATEGIC PLAN       ")
                print("=========================================")
                print(f"Current Price: {current_price}")
                print(f"Market Structure Trend: {trend.upper()}")
                print(f"Premium/Discount 50% Eq: {midline}\n")
                
                print("--- SCENARIOS ---")
                
                # 1. BULLISH PLAN
                print(f"Plan 1: Bullish Continuation")
                if high_prob_bullish:
                    best_long = high_prob_bullish[-1]
                    print(f"-> Setup exists: FVG detected. IF price retraces down to {best_long[1]} in the Discount Zone, execute LONG.")
                    if best_long[2]:
                        print(f"-> Confluence: Backed by Order Block at {best_long[2]}.")
                else:
                    print("-> No Bullish FVG+OB setup found yet. Wait for a new Swing Low to form before looking for longs.")
                print()
                
                # 2. BEARISH PLAN
                print(f"Plan 2: Bearish Continuation")
                if high_prob_bearish:
                    best_short = high_prob_bearish[-1]
                    print(f"-> Setup exists: FVG detected. IF price pumps to {best_short[0]} in the Premium Zone, execute SHORT.")
                    if best_short[2]:
                        print(f"-> Confluence: Guarded by Institutional Order Block at {best_short[2]}.")
                else:
                    print("-> No Bearish FVG+OB setup found yet. Wait for a fakeout pump to form a supply zone.")
                print()
                
                # 3. NEUTRAL / TRAP AVOIDANCE PLAN
                print(f"Plan 3: Neutral / Trap Avoidance")
                if trend == "Bullish":
                    print(f"-> IF price violently crashes below {swing_lows[-1]['low']}, the Bullish trend is DEAD. Do NOT take longs. Expect a reversal.")
                elif trend == "Bearish":
                    print(f"-> IF price aggressively breaks above {swing_highs[-1]['high']}, the Bearish trend is DEAD. Cancel all Shorts. Wait for structure shift.")
                else:
                    print(f"-> Ranging Market. IF price breaks above {swing_highs[-1]['high']} or below {swing_lows[-1]['low']}, wait for an FVG to form on the breakout and trade the pullback.")
                print()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    scan_advanced_smc(r'C:\Users\nagas\.gemini\antigravity\brain\8fccdb21-bf83-46dc-b730-edd803c88713\.system_generated\steps\1211\output.txt')
