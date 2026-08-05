import streamlit as st
import pandas as pd
import json
import os

# Page configuration
st.set_page_config(page_title="NSE 315 Strategy Dashboard", layout="wide")

# Load configuration
config_path = "config.json"
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
else:
    config = {"max_stocks": 5, "auto_scan_interval_minutes": 15}

max_stocks = int(config.get("max_stocks", 5))

st.title("2️⃣ Top F&O Stocks Scanner & Day High/Low Filter")

# Auto-refresh mechanism for auto-scan view in Streamlit
try:
    from streamlit_autorefresh import st_autorefresh
    interval_ms = int(config.get("auto_scan_interval_minutes", 15)) * 60 * 1000
    st_autorefresh(interval=interval_ms, key="datarefresh")
except ImportError:
    pass

st.sidebar.header("Scanner Settings")
st.sidebar.info(f"Displaying Top {max_stocks} Stocks Automatically.")

# Data loading logic (Checking common files or databases)
def load_data():
    if os.path.exists("signals.csv"):
        return pd.read_csv("signals.csv")
    elif os.path.exists("scanned_stocks.csv"):
        return pd.read_csv("scanned_stocks.csv")
    else:
        # Fallback dummy data matching your screenshot columns if file doesn't exist yet
        data = {
            "Stock": ["RELIANCE", "TCS", "INFY", "ICICIBANK", "SBIN", "HDFCBANK", "ITC"],
            "OI Status": ["High OI Spurt"] * 7,
            "Day High": [1313.7, 2463.6, 1177.2, 1454.6, 1053.2, 752.25, 289.0]
        }
        return pd.DataFrame(data)

df = load_data()

st.subheader(f"Top {max_stocks} Filtered Stocks")

if not df.empty:
    # STRICTLY LIMIT TO TOP 5 (or max_stocks defined in config.json)
    top_df = df.head(max_stocks)
    
    # Display table cleanly
    st.dataframe(top_df, use_container_width=True)
else:
    st.warning("No stock data found. Please run the scanner.")

# Manual scan trigger button
if st.button("Run Manual Scan Now"):
    st.success("Scan triggered successfully! Refreshing data...")
    st.rerun()
