# 📊 Projeto de Visualização de Ações da B3 com FastAPI e Streamlit

Este projeto integra uma API criada com FastAPI e uma interface de visualização com Streamlit para exibir dados de ações listadas na B3 (Bolsa de Valores do Brasil).

## 🚀 Funcionalidades

- **API FastAPI**: Fornece endpoints para buscar todos os tickers listados e filtrar informações por ticker específico.
- **Interface Streamlit**: Permite a visualização dos dados das ações, incluindo gráficos de preços históricos utilizando a API do Yahoo Finance.

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e de alto desempenho para construir APIs com Python.
- **Streamlit**: Ferramenta para criar aplicações web interativas e de fácil utilização com Python.
- **Pandas**: Biblioteca poderosa para manipulação de dados.
- **Plotly**: Biblioteca gráfica utilizada para visualização de dados.
- **Yahoo Finance (yfinance)**: Biblioteca para obtenção de dados financeiros diretamente do Yahoo Finance.

## 📂 Estrutura do Projeto

```bash
├── api.py               # Código da API FastAPI
├── app.py               # Código da interface Streamlit
├── acoes-listadas-b3.csv # Arquivo CSV contendo os dados das ações listadas
└── README.md            # Arquivo de documentação do projeto
