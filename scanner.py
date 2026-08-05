import time
import json
import os

def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return {"auto_scan_interval_minutes": 15, "max_stocks": 5}

def run_scanner():
    print("Market Scanner Started...")
    # Aapka actual scanning logic yahan aayega
    # Jaise: fetch market data, apply 315 strategy indicators, sort and save top results.
    
    # Example saving to CSV for dashboard
    # top_stocks.head(config["max_stocks"]).to_csv("signals.csv", index=False)
    pass

if __name__ == "__main__":
    config = load_config()
    interval_seconds = config.get("auto_scan_interval_minutes", 15) * 60
    
    print(f"Auto-scan initialized. Interval: {config.get('auto_scan_interval_minutes', 15)} minutes.")
    
    while True:
        try:
            run_scanner()
            print(f"Scan completed. Waiting for {config.get('auto_scan_interval_minutes', 15)} minutes...")
        except Exception as e:
            print(f"Error during scanning: {e}")
            
        time.sleep(interval_seconds)
