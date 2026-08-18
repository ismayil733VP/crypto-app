
import streamlit as st
import pandas as pd

import requests

st.set_page_config(page_title="Crypto Analysis", layout="wide")
st.title("📈 Crypto Analysis Dashboard")

@st.cache_data
def get_data():
    url = "https://data-api.binance.vision/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=100"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'QAV', 'NAT', 'TBBAV', 'TBQAV', 'Ignore'])
    df['Close'] = pd.to_numeric(df['Close'])
    
    
    return df

df = get_data()

st.write("### BTCUSDT 1H Chart")
st.line_chart(df[['Close']])

