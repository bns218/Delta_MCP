import time
import requests
from datetime import datetime, time as datetime_time

class SMCScalper:
    def __init__(self, symbol="BTCUSD", timeframes=["5m", "15m", "1h"]):
        self.symbol = symbol
        self.timeframes = timeframes
        self.api_url = "https://api.delta.exchange/v2/history/candles"
        
        # Killzones in IST (Indian Standard Time)
        self.killzones = [
            {"name": "London", "start": datetime_time(12, 30), "end": datetime_time(15, 30)},
            {"name": "New York", "start": datetime_time(18, 30), "end": datetime_time(21, 30)}
        ]

    def is_in_killzone(self):
        """Checks if the current time in IST falls within an active Killzone."""
        now = datetime.now().time()
        for kz in self.killzones:
            if kz["start"] <= now <= kz["end"]:
                return True, kz["name"]
        return False, "Out of Session"

    def get_recent_candles(self, timeframe):
        end_time = int(time.time())
        start_time = end_time - (60 * 60 * 24)
        
        params = {
            "symbol": self.symbol,
            "resolution": timeframe,
            "start": start_time,
            "end": end_time
        }
        
        try:
            response = requests.get(self.api_url, params=params)
            data = response.json()
            if "result" in data:
                return sorted(data["result"], key=lambda x: x["time"])
        except Exception as e:
            print(f"Error fetching data: {e}")
        return []

    def scan_for_fvgs(self, candles):
        active_fvgs = []
        for i in range(len(candles) - 2):
            c1, c2, c3 = candles[i], candles[i+1], candles[i+2]
            
            if c1['low'] > c3['high']:
                active_fvgs.append({
                    "type": "Bearish", "top": c1['low'], "bottom": c3['high'],
                    "gap_size": c1['low'] - c3['high'], "timestamp": c2["time"]
                })
            elif c1['high'] < c3['low']:
                active_fvgs.append({
                    "type": "Bullish", "top": c3['low'], "bottom": c1['high'],
                    "gap_size": c3['low'] - c1['high'], "timestamp": c2["time"]
                })
        return active_fvgs

    def run(self):
        print(f"Starting SMC Golden Intraday Bot for {self.symbol} (Scalp: 3m | Intraday: 5m, 1h)")
        print("Bot will strictly filter for London & New York Killzones.")
        
        while True:
            in_killzone, session_name = self.is_in_killzone()
            now_str = datetime.now().strftime('%H:%M:%S')
            
            if not in_killzone:
                print(f"[{now_str}] Ignoring Asian/Dead Session. Waiting for Killzone...")
            else:
                print(f"\n[{now_str}] ACTIVE KILLZONE ({session_name}). Hunting setups...")
                
                # Check all timeframes according to user strategy
                strategy_timeframes = {"3m": "SCALP", "5m": "INTRADAY", "1h": "INTRADAY"}
                
                for tf, strategy_type in strategy_timeframes.items():
                    candles = self.get_recent_candles(tf)
                    if len(candles) >= 3:
                        fvgs = self.scan_for_fvgs(candles)
                        if fvgs:
                            latest = fvgs[-1]
                            print(f"[{tf} {strategy_type}] ALERT: {latest['type']} FVG Detected in {session_name} Session!")
                            print(f"   Zone: ${latest['bottom']} - ${latest['top']}")
                            
            time.sleep(60)

if __name__ == "__main__":
    bot = SMCScalper(symbol="BTCUSD")
    bot.run()
