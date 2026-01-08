import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Backtesting App")

# ======================
# Data Source
# ======================
source = st.radio("Select data source", ["Yahoo Finance", "CSV Upload"])
df = None

if source == "Yahoo Finance":
    symbol = st.text_input("Symbol", "BTC-USD")
    period = st.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y"], index=3)
    interval = st.selectbox("Interval", ["15m", "30m", "1h", "4h", "1d"], index=2)

    if st.button("Load Data"):
        df = yf.download(symbol, period=period, interval=interval, progress=False)

else:
    file = st.file_uploader("Upload CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)

# ======================
# Strategy Parameters
# ======================
st.subheader("Strategy Parameters")

fast_sma = st.slider("Fast SMA Length", 5, 50, 10)
slow_sma = st.slider("Slow SMA Length", 10, 200, 30)

if slow_sma <= fast_sma:
    st.warning("Slow SMA should be greater than Fast SMA")

# ======================
# Show Data
# ======================
if df is not None and not df.empty:
    st.success(f"Loaded {len(df)} rows")
    st.dataframe(df.tail(20))
