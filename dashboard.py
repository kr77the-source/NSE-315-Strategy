import streamlit as st
import pandas as pd
from market import MarketOverview
from scanner import StockScanner
from risk_manager import RiskManager
from strategy import StrategyAnalytics

def render_dashboard():
    st.set_page_config(page_title="Master Sequential Trading System", layout="wide")
    st.title("🚀 Master 5-Stage Heikin-Ashi Execution Dashboard")
    st.markdown("---")
    
    col_label, col_val = st.columns([2, 8])
    with col_label:
        st.markdown("### 1️⃣ Market Overview:")
    with col_val:
        market_data = MarketOverview.get_market_bias()
        bias = market_data["market_bias"]
        if bias == "BULLISH":
            st.success(f"**{bias}**")
        else:
            st.warning(f"**{bias}**")
        
    st.markdown("---")
    
    st.header("2️⃣ Top 5 F&O Stocks Shortlisted (Stage 2)")
    top_stocks_data = StockScanner.get_top_stocks(bias)
    st.dataframe(pd.DataFrame(top_stocks_data), use_container_width=True)
    
    st.markdown("---")
    
    st.header("3️⃣ High/Low Breakout Confirmation (Stage 3)")
    breakouts_data = StockScanner.check_breakouts(top_stocks_data)
    st.dataframe(pd.DataFrame(breakouts_data), use_container_width=True)
    
    st.markdown("---")
    
    st.header("4️⃣ Trade Execution: Entry Price & Stop-Loss (Stage 4)")
    trades_data = RiskManager.calculate_trade_levels(breakouts_data)
    st.dataframe(pd.DataFrame(trades_data), use_container_width=True)
    
    st.markdown("---")
    
    st.header("5️⃣ Strategy Backtest Results & Analytics (Stage 5)")
    backtest = StrategyAnalytics.get_backtest_results()
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Backtest Win Rate", value=backtest["win_rate"])
    with c2:
        st.metric(label="Profit Factor", value=backtest["profit_factor"])
    with c3:
        st.metric(label="Max Drawdown", value=backtest["max_drawdown"])
    with c4:
        st.metric(label="System Status", value=backtest["status"])