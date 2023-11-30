import requests
from bs4 import BeautifulSoup
import pandas as pd
#import time

# - pesquisa 1 (Sobre os indicadores de crescimento CAGR):

tickers = ['ddnb34', 'dxco3', 'ddnb34']
#ticker = tickers[0]
# print(ticker)
# print(ticker[-2:])

for ticker in tickers:
    link = "https://statusinvest.com.br/bdrs/"+ticker # VARIA: "bdrs" e "acoes"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    print(requisicao)

# for ticker in tickers:
#     print(ticker[-2:])
#     print(type(ticker[-2:]))

#     if ticker[-2] == '34':
#         # 1 - se terminar em 34, fazer requisição para link de bdrs
#         link = "https://statusinvest.com.br/bdrs/"+ticker # VARIA: "bdrs" e "acoes"
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
#         requisicao = requests.get(link, headers=headers)
#         site = BeautifulSoup(requisicao.text, "html.parser")
#         print(requisicao)
#     else:
#         # 1 - se não terminar em 34, fazer requisição para link de acoes
#         link = "https://statusinvest.com.br/acoes/"+ticker # VARIA: "bdrs" e "acoes"
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
#         requisicao = requests.get(link, headers=headers)
#         site = BeautifulSoup(requisicao.text, "html.parser")
#         print(requisicao)

