import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8501"],  # Ajuste para o seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
lista = pd.read_csv("acoes-listadas-b3.csv")
df = pd.DataFrame(lista)

@app.get("/buscar/all")
async def get_all():
    tickers = df["Ticker"].tolist()
    data = [{"Ticker": ticker} for ticker in tickers]
    return JSONResponse(content={"Tickers": data})


@app.get("/buscar/")
async def get_ticker(ticker: str):
    filtered_df = df[df["Ticker"] == ticker]
    data = filtered_df.to_dict(orient="records")
    return JSONResponse(content={"Ticker": data})


if __name__ == "__main__":
    uvicorn.run(app, port=8000)