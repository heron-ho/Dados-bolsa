import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


empresas = pd.read_excel('empresas-info.xlsx')
empresas_tickers = empresas['symbol'].str.strip()
print(empresas_tickers)


# - pesquisa 1 (Sobre os indicadores de crescimento CAGR):
respostas_CAGR_RECEITA = []
respostas_CAGR_LUCRO = []
contador = 0

for ticker in empresas_tickers:
    try:
        # 1 - Fazer requisição
        link = "https://statusinvest.com.br/acoes/"+ticker # VARIA: "bdrs" e "acoes"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
        requisicao = requests.get(link, headers=headers)
        site = BeautifulSoup(requisicao.text, "html.parser")
        print(requisicao)

        # 2 - Coletando os dados (raspagem)
        div1 = site.find("div", title="O CAGR (Compound Annual Growth Rate), ou taxa de crescimento anual composta, é a taxa de retorno necessária para um investimento crescer de seu saldo inicial para o seu saldo final.")
        Strong_da_div1 = div1.find("strong").text

        div2 = site.find_all("div", title="O CAGR (Compound Annual Growth Rate), ou taxa de crescimento anual composta, é a taxa de retorno necessária para um investimento crescer de seu saldo inicial para o seu saldo final.")[1]
        Strong_da_div2 = div2.find("strong").text

        print(f"INDICADOR DE CRESCIMENTO:\nCAGR receita ultimos 5 anos: {Strong_da_div1},\nCAGR lucro ultimos 5 anos: {Strong_da_div2}")
        respostas_CAGR_RECEITA.append(Strong_da_div1)
        respostas_CAGR_LUCRO.append(Strong_da_div2)
        contador += 1
        time.sleep(1)
        
        # 3 - Realizando prints dos idens obtidos   
        #print("lista de indicadores da empresa para adicionar à planilha:")
        #print(respostas_CAGR_RECEITA)
        #print(respostas_CAGR_LUCRO)
    except AttributeError as error:
        print(f'AttributeError no item {contador}')
    except:    
        print(f'Algum erro no item {contador}')
    else:
        print(f'sem erros no item {contador}')
    finally:
        print(f"item nº: {contador} - PRONTO\n-----------------------")
        
        

# - Salvando em arquivos excel os dados
empresas['CAGR RECEITAS 5 ANOS'] = pd.Series(respostas_CAGR_RECEITA)
empresas['CAGR LUCROS 5 ANOS'] = pd.Series(respostas_CAGR_LUCRO)
print(empresas)
empresas.to_excel("empresas_br_indicadores.xlsx")

