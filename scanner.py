import yfinance as yf
import pandas as pd

class StockScanner:
    @staticmethod
    def get_top_stocks(bias):
        # Top NSE F&O stocks symbols for live tracking
        symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "ICICIBANK.NS", "SBIN.NS"]
        live_data = []
        
        for symbol in symbols:
            try:
                ticker = yf.Ticker(symbol)
                df = ticker.history(period="1d", interval="15m")
                if not df.empty:
                    high = df['High'].max()
                    low = df['Low'].min()
                    close = df['Close'].iloc[-1]
                    name = symbol.replace(".NS", "")
                    live_data.append({
                        "stock": name,
                        "oi_status": "Live Tracking",
                        "day_high": round(high, 2),
                        "day_low": round(low, 2),
                        "current_price": round(close, 2)
                    })
            except Exception:
                continue
        return live_data

    @staticmethod
    def check_breakouts(top_stocks):
        breakout_results = []
        for item in top_stocks:
            curr = item.get("current_price", 0)
            high = item.get("day_high", 0)
            
            # Agar current price day high ke paas ya cross kar raha hai
            b_type = "HIGH BREAKOUT 🚀" if curr >= (high * 0.995) else "Consolidating ⏳"
            breakout_results.append({
                "stock": item["stock"],
                "breakout_type": b_type,
                "trigger_price": high,
                "status": "Active Live"
            })
        return breakout_results
