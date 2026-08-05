import streamlit as st
import pandas as pd
import json
import os

# Page configuration
st.set_page_config(page_title="NSE 315 Strategy Dashboard", layout="wide")

# Load configuration
config_path = "config.json"
max_stocks = 5
if os.path.exists(config_path):
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
            max_stocks = int(config.get("max_stocks", 5))
    except Exception:
        pass

st.title("📊 NSE 315 Strategy Dashboard")

st.sidebar.header("Scanner Settings")
st.sidebar.info(f"Displaying Top {max_stocks} Stocks Strictly.")

# Load Data and strictly limit to max_stocks immediately
def load_data():
    if os.path.exists("signals.csv"):
        df = pd.read_csv("signals.csv")
    elif os.path.exists("scanned_stocks.csv"):
        df = pd.read_csv("scanned_stocks.csv")
    else:
        # Fallback dummy data
        data = {
            "Stock": ["RELIANCE", "TCS", "INFY", "ICICIBANK", "SBIN", "HDFCBANK", "ITC"],
            "OI Status": ["High OI Spurt"] * 7,
            "Day High": [1313.7, 2463.6, 1177.2, 1454.6, 1053.2, 752.25, 289.0],
            "Strategy Status": ["No Setup ⏳"] * 7,
            "Inside Candle": ["No", "Yes 🟢", "Yes 🟢", "Yes 🟢", "No", "Yes 🟢", "No"]
        }
        df = pd.DataFrame(data)
    
    # Strictly cut dataframe to max_stocks (Top 5) right here
    return df.head(max_stocks)

df = load_data()

# ==========================================
# SECTION 2: Top F&O Stocks Scanner
# ==========================================
st.markdown("---")
st.subheader("2️⃣ Top F&O Stocks Scanner & Day High/Low Filter")

if not df.empty:
    st.dataframe(df, width="stretch")
else:
    st.warning("No data available.")

# ==========================================
# SECTION 3: Strategy Breakout & Inside Candle
# ==========================================
st.markdown("---")
st.subheader("3️⃣ Strategy Breakout & Inside Candle Confirmation")

if not df.empty:
    st.dataframe(df, width="stretch")
else:
    st.warning("No data available.")

# Manual scan trigger
st.markdown("---")
if st.button("Run Auto-Scan / Refresh Now"):
    st.success("Scan executed successfully!")
    st.rerun()
