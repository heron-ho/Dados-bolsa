import requests
from bs4 import BeautifulSoup
import pandas as pd
#import time

# - preparar tabela de empresas fontes para a pesquisa

# tabela - empresas
empresas = pd.read_excel("empresa-ticker-arrumado.xlsx")
print(empresas)

#tabela - tickers
tickers = pd.read_excel("empresa-ticker-arrumado.xlsx")["ticker"]
tickers = tickers.str.strip()
print(tickers)

# - pesquisa:
respostas = []

for ticker in tickers:
    
    
    # 1 - Fazer requisição
    link = "https://statusinvest.com.br/acoes/"+ticker # VARIA: "bdrs" e "acoes"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
    requisicao = requests.get(link, headers=headers)
    site = BeautifulSoup(requisicao.text, "html.parser")
    print(requisicao)
    

    # 2 - Coletando os dados (raspagem)
    div1 = site.find("div", title="O CAGR (Compound Annual Growth Rate), ou taxa de crescimento anual composta, é a taxa de retorno necessária para um investimento crescer de seu saldo inicial para o seu saldo final.")
    Strong_da_div1 = div1.find("strong").text

    print("INDICADOR DE CRESCIMENTO: " + Strong_da_div1)
    respostas.append(Strong_da_div1)
    
print("lista de indicadores para adicionar à planilha:")
print(respostas)
empresas['crescimento'] = respostas
print(empresas)
empresas.to_excel("empresas_com_indicadores.xlsx")



    