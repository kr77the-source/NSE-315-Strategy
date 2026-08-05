import os
import json
import pandas as pd
import time

def load_config():
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {"max_stocks": 5, "auto_scan_interval_minutes": 15}

def main():
    print("Initializing NSE 315 Strategy Main Module...")
    config = load_config()
    max_stocks = int(config.get("max_stocks", 5))
    
    # Ensure any generated CSV/database output strictly obeys max_stocks limit
    signals_file = "signals.csv"
    if os.path.exists(signals_file):
        df = pd.read_csv(signals_file)
        if len(df) > max_stocks:
            df = df.head(max_stocks)
            df.to_csv(signals_file, index=False)
            print(f"Trimmed signals.csv to top {max_stocks} stocks.")

if __name__ == "__main__":
    main()
