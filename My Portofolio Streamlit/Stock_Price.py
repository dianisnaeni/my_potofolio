import pandas as pd
import streamlit as st
import yfinance as yf

st.write("""
# Simple Stock Price App

shown are the stock closing price and volume Google!
""")

tickerSymbol = 'GOOGL'

tickerData= yf.Ticker(tickerSymbol)

tickerDF= tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)