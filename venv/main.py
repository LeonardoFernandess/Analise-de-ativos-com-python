import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import requests

st.set_page_config(layout="wide")

api_url = "http://127.0.0.1:8000/buscar/"

# Obtendo a lista de todos os tickers
response = requests.get(f"{api_url}all")
if response.status_code == 200:
    tickers_data = response.json()["Tickers"]
    tickers_opcoes = ["Todos"] + [ticker["Ticker"] for ticker in tickers_data]
else:
    st.error("Erro ao carregar os dados de tickers.")
    tickers_opcoes = ["Todos"]

# Seleção do ticker
ticker_selecionado = st.sidebar.selectbox("ATIVO", tickers_opcoes, index=0)

# Filtrando os dados com base no ticker selecionado
if ticker_selecionado == "Todos":
    df_filtrado = pd.DataFrame(tickers_data)
else:
    response = requests.get(f"{api_url}?ticker={ticker_selecionado}")
    if response.status_code == 200:
        df_filtrado = pd.DataFrame(response.json()["Ticker"])
    else:
        st.error("Erro ao carregar os dados do ticker.")
        df_filtrado = pd.DataFrame()

st.write(df_filtrado)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

def upload_data(ticker):
    tic = yf.Ticker(f"{ticker}.SA").history("1y")
    tic.reset_index(inplace=True)
    tic['ticker'] = ticker.split(".")[0]
    return tic

# Verifica se apenas um ticker está selecionado para obter os dados
if ticker_selecionado != "Todos":
    ticker_fil = upload_data(ticker_selecionado)
    st.write(ticker_fil)
    fig_ticker = px.bar(ticker_fil, x="Date", y="Close", color="Open", title="Fechamento")
    col1.plotly_chart(fig_ticker)
