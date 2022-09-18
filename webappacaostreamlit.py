# ok - Abrindo no Chorme o App Web
# streamlit run webappacaostreamlit.py
# OKS
# pip install streamlit
# pip install gspread
# pip install matplotlib
# pip install bokeh
# pip install plotly
# pip install plot
# pip install sklearn
# pip install yfinance

#pip install gunicorn ->Para o 1º deploy
#pip freeze > requirements.txt
# heroku create webappacaostreamlit --buildpack heroku/python
# pip install pypiwin32
# ver passo a passo do heroku-> https://dashboard.heroku.com/apps/tamarazoner/deploy/heroku-git

# Biblioteca
from AnaliseComYahoo import Analise
import streamlit as st

# %%writefile app.py

LANGUAGE_CODE = 'pt-br'
USE_I18N = True

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione uma opção',
                                         ['Analise Com Yahoo'])
st.title('**Web App de Analise de Ações**')


if paginaSelecionada == 'Analise Com Yahoo':
    Yahoo = Analise()
