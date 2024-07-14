import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Stock Market View App
""")

# st.write("""
# Here are the price of the Stock Market of Apple!
# """
# )

def getPrice(tickerSymbol):
    # Get the data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the price on specific date on thie stock
    tickerDf = tickerData.history(period='1d', start='2000-06-20', end='2020-06-20')
    return tickerDf

# Apple Stock Market
st.write("""
Here are the price of the **Apple** Stock Market from ***2010 to 2020***
""")

AAPL = getPrice('AAPL')

st.line_chart(AAPL.Close)
st.line_chart(AAPL.Volume)

# Tesla Stock Market
st.write("""
Here are the price of the **Tesla** Stock Market from ***2010 to 2020***
""")

TSLA = getPrice('TSLA')

st.line_chart(TSLA.Close)
st.line_chart(TSLA.Volume)