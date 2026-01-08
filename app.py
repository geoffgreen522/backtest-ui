import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Backtesting App – Data Loader")

# --- Yahoo Finance inputs ---
symbol = st.text_input("Symbol", "BTC-USD")
period = st.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y"], index=3)
interval = st.selectbox("Interval", ["15m", "30m", "1h", "4h", "1d"], index=2)

# --- Load data ---
if st.button("Load Yahoo Finance Data"):
    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        progress=False
    )

    if df.empty:
        st.error("No data returned. Try a different symbol or interval.")
    else:
        st.success(f"Loaded {len(df)} rows of data")
        st.dataframe(df.tail(50))
