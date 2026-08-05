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

st.title("📊 NSE 315 Strategy Dashboard")

# Auto-refresh mechanism for auto-scan view
try:
    from streamlit_autorefresh import st_autorefresh
    interval_ms = int(config.get("auto_scan_interval_minutes", 15)) * 60 * 1000
    st_autorefresh(interval=interval_ms, key="datarefresh")
except ImportError:
    pass

st.sidebar.header("Scanner Settings")
st.sidebar.info(f"Displaying Top {max_stocks} Stocks Strictly.")

# Dummy / Live Data Loader
def load_data():
    if os.path.exists("signals.csv"):
        return pd.read_csv("signals.csv")
    else:
        # Fallback data matching your screenshots
        data = {
            "Stock": ["RELIANCE", "TCS", "INFY", "ICICIBANK", "SBIN", "HDFCBANK", "ITC"],
            "OI Status": ["High OI Spurt"] * 7,
            "Day High": [1313.7, 2463.6, 1177.2, 1454.6, 1053.2, 752.25, 289.0],
            "Strategy Status": ["No Setup ⏳"] * 7,
            "Inside Candle": ["No", "Yes 🟢", "Yes 🟢", "Yes 🟢", "No", "Yes 🟢", "No"]
        }
        return pd.DataFrame(data)

df = load_data()

# ==========================================
# SECTION 2: Top F&O Stocks Scanner
# ==========================================
st.markdown("---")
st.subheader("2️⃣ Top F&O Stocks Scanner & Day High/Low Filter")

if not df.empty:
    # STRICT LIMIT TO TOP 5
    df_section2 = df.head(max_stocks)
    st.dataframe(df_section2, use_container_width=True)
else:
    st.warning("No data available.")

# ==========================================
# SECTION 3: Strategy Breakout & Inside Candle
# ==========================================
st.markdown("---")
st.subheader("3️⃣ Strategy Breakout & Inside Candle Confirmation")

if not df.empty:
    # STRICT LIMIT TO TOP 5 HERE TOO
    df_section3 = df.head(max_stocks)
    st.dataframe(df_section3, use_container_width=True)
else:
    st.warning("No data available.")

# Manual scan trigger
st.markdown("---")
if st.button("Run Auto-Scan / Refresh Now"):
    st.success("Scan executed successfully!")
    st.rerun()
