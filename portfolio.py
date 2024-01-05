
from datetime import datetime
import streamlit as st
import pandas as pd
import yfinance as yf
import requests
import plotly.express as px
import matplotlib.pyplot as plt

# Streamlit app title
st.title("Portfolio Performance Viewer")


# Create a session with proxies
session = requests.Session()
session.proxies = proxies

# Define the list of tickers
tickers_list = "36BZ.DE MTPI.PA BTC-EUR VNRA.DE EGLN.L EUNK.DE"
tickers = yf.Tickers(tickers_list)

# Download closing prices
closing_prices = tickers.history(start="2024-01-04")["Close"].ffill()

# Define initial capital and fee
capital = 2500
cash = 355.27
fee = 13

# Define loading prices and the number of stocks for each ticker
loading_prices = pd.Series({
    "36BZ.DE": 3.6695,
    "MTPI.PA": 4.4349,
    "BTC-EUR": 41064.5216,
    "VNRA.DE": 105.08,
    "EGLN.L": 36.416,
    "EUNK.DE": 71.64
})

n_stocks = pd.Series({
    "36BZ.DE": 140,
    "MTPI.PA": 68,
    "BTC-EUR": 0.00599724,
    "VNRA.DE": 6,
    "EGLN.L": 9,
    "EUNK.DE": 5
})

name_mapping = {
    "36BZ.DE": "ETF China",
    "MTPI.PA": "ETF EM",
    "BTC-EUR": "BTC",
    "VNRA.DE": "ETF North America",
    "EGLN.L": "Gold",
    "EUNK.DE": "ETF Europe"

}
# Calculate the initial portfolio value
loading_prices = loading_prices @ n_stocks
portfolio_value = closing_prices * n_stocks
portfolio_value.columns = [name_mapping[i] for i in portfolio_value.columns]
portfolio_value["cash"] = cash
portfolio_value.dropna(inplace=True)

p_l = portfolio_value.sum(axis=1) - 2750
portfolio_value.iloc[-1].T.plot.pie(ylabel="")
# Streamlit plot
st.line_chart(p_l, use_container_width=True)

fig = px.pie(
    values=portfolio_value.iloc[-1].values,
    names=portfolio_value.columns,
    title="Portfolio Allocation"
)
st.plotly_chart(fig)

st.line_chart((portfolio_value.drop("cash",axis=1)-14)/loading_prices, use_container_width=True)

# Display portfolio performance summary
ret = p_l.iloc[-1]/loading_prices * 100
st.write(f"Final Portfolio Value: {portfolio_value.iloc[-1].sum():.2f}")
if ret > 0: st.success(f"Portfolio Return: {ret:.2f}%")
else: st.warning(f"Portfolio Return: {ret:.2f}%")
st.write(f"Portfolio Return (no fee): {(p_l.iloc[-1]+fee)/loading_prices * 100:.2f}%")
st.write(f"Portfolio P&L: {p_l.iloc[-1]}")
