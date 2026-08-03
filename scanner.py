class StockScanner:
    @staticmethod
    def get_top_stocks(bias):
        # Stage 2: Top 5 F&O Stocks Screening
        if bias == "BULLISH":
            return [
                {"stock": "RELIANCE", "oi_status": "Long Buildup", "day_high": 2520.0, "day_low": 2480.0},
                {"stock": "TCS", "oi_status": "Short Covering", "day_high": 3220.0, "day_low": 3170.0},
                {"stock": "INFY", "oi_status": "Long Buildup", "day_high": 1460.0, "day_low": 1435.0},
                {"stock": "ICICIBANK", "oi_status": "Long Buildup", "day_high": 1100.0, "day_low": 1080.0},
                {"stock": "SBIN", "oi_status": "Long Buildup", "day_high": 820.0, "day_low": 805.0}
            ]
        return []

    @staticmethod
    def check_breakouts(top_stocks):
        # Stage 3: High/Low Breakout Confirmation
        breakout_results = []
        for item in top_stocks:
            breakout_results.append({
                "stock": item["stock"],
                "breakout_type": "HIGH BREAKOUT 🚀",
                "trigger_price": item["day_high"] + 2.0,
                "status": "Confirmed"
            })
        return breakout_results