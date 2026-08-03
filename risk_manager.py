class RiskManager:
    @staticmethod
    def calculate_trade_levels(breakouts):
        active_trades = []
        for b in breakouts:
            trigger = b["trigger_price"]
            active_trades.append({
                "stock": b["stock"],
                "action": "BUY",
                "entry_price": trigger,
                "stop_loss": round(trigger * 0.985, 2),
                "target": round(trigger * 1.03, 2)
            })
        return active_trades