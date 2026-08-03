import yfinance as yf

class MarketOverview:
    @staticmethod
    def get_market_bias():
        try:
            # Nifty 50 live data check karenge market trend ke liye
            nifty = yf.Ticker("^NSEI")
            df = nifty.history(period="5d", interval="1d")
            if not df.empty:
                current_close = df['Close'].iloc[-1]
                prev_close = df['Close'].iloc[-2]
                bias = "BULLISH" if current_close > prev_close else "BEARISH"
                return {"market_bias": bias, "nifty_price": round(current_close, 2)}
        except Exception:
            pass
        return {"market_bias": "BULLISH", "nifty_price": 0.0}
