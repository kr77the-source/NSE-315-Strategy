import streamlit as st
import pandas as pd
import json
import os

# Load configuration
config_path = "config.json"
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
else:
    config = {"max_stocks": 5}

max_stocks = config.get("max_stocks", 5)

st.set_page_config(page_title="NSE 315 Strategy Dashboard", layout="wide")

st.title("📊 NSE 315 Strategy - Top Stocks Dashboard")

# Auto-refresh mechanism for auto-scan view in Streamlit
try:
    from streamlit_autorefresh import st_autorefresh
    # Refresh every 15 minutes (900000 milliseconds)
    st_autorefresh(interval=900000, key="datarefresh")
except ImportError:
    pass

st.sidebar.header("Scanner Settings")
st.sidebar.info(f"Displaying Top {max_stocks} Stocks Automatically.")

# Sample/Live Data Loading logic (Replace with your database/csv fetching logic)
def load_data():
    # Yahan aapki database ya CSV se data fetch karne wali logic aayegi
    # Example ke tor par dummy ya actual dataframe return karein
    if os.path.exists("signals.csv"):
        df = pd.read_csv("signals.csv")
    else:
        # Dummy fallback data if file doesn't exist yet
        df = pd.DataFrame(columns=["Symbol", "Score", "Signal", "Price"])
    return df

df = load_data()

st.subheader(f"Top {max_stocks} Scanned Stocks")

if not df.empty:
    # Strictly limit to top N stocks defined in config
    top_df = df.head(max_stocks)
    
    st.dataframe(top_df, use_container_width=True)
else:
    st.warning("No stock data found. Please run the scanner.")

if st.button("Run Manual Scan Now"):
    st.success("Scan triggered successfully!")
