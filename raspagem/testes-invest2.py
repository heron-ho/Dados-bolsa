import requests
from bs4 import BeautifulSoup
import pandas as pd
#import time

empresas = pd.read_excel('empresas-info-testes.xlsx')
empresas_tickers = empresas['symbol'].str.strip()
print(empresas_tickers)

tickers = empresas_tickers
acoes_ou_bdrs = []

for ticker in tickers:
    
    # 1 - faz requisição
    link = "https://statusinvest.com.br/acoes/"+ticker # VARIA: "bdrs" e "acoes"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    print(requisicao)

    if (requisicao.status_code != 200):
        acoes_ou_bdrs.append('deve-ser-bdr')

        # 1 - faz requisição para brs
        link = "https://statusinvest.com.br/bdrs/"+ticker # VARIA: "bdrs" e "acoes"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        requisicao = requests.get(link, headers=headers)
        site = BeautifulSoup(requisicao.text, "html.parser")
        print(requisicao)
    else:
        print('deve-ser-acao')
        acoes_ou_bdrs.append('acao')

empresas['tipo-de-acao'] = pd.Series(acoes_ou_bdrs)
empresas.to_excel('empresas_br_tipos-teste.xlsx')
    


