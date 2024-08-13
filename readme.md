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

├── venv/                # Ambiente virtual com as dependências instaladas

├── api.py               # Código da API FastAPI

├── app.py               # Código da interface Streamlit

├── acoes-listadas-b3.csv # Arquivo CSV contendo os dados das ações listadas

├── requirements.txt     # Arquivo com as dependências do projeto

└── README.md            # Arquivo de documentação do projeto

```

## ⚙️ Como Executar

### 1. Configurar o Ambiente Virtual

Certifique-se de ter Python 3.7+ instalado. Navegue até o diretório do projeto e crie um ambiente virtual:

```bash

python -m venv venv

```

Ative o ambiente virtual:

- **No Windows:**

```bash

venv\Scripts\activate

```

- **No macOS/Linux:**

```bash

source venv/bin/activate

```

Instale as dependências necessárias usando o arquivo `requirements.txt`:

```bash

pip install -r requirements.txt

```

### 2. Executar a API FastAPI

No terminal, com o ambiente virtual ativado, navegue até o diretório onde o arquivo `api.py` está salvo e execute:

```bash

uvicorn api:app --reload

```

A API estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 3. Executar a Interface Streamlit

Em um novo terminal, com o ambiente virtual ativado, navegue até o diretório onde o arquivo `app.py` está salvo e execute:

```bash

streamlit run main.py

```

A interface estará disponível em [http://localhost:8501](http://localhost:8501).

## 📊 Uso da Aplicação

- **Selecionar Ativo:** Use o menu lateral para selecionar um ticker específico ou "Todos" para ver a lista completa de ações.
- **Visualizar Dados:** Selecione um ticker específico para visualizar os dados históricos e gráficos interativos.
- **Análise Gráfica:** Explore os gráficos gerados pelo Plotly, que mostram o preço de fechamento e outros dados relevantes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
