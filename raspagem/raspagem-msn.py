from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Utilizando o webdriver

browser = webdriver.Firefox()
browser.get('https://www.msn.com/pt-br/dinheiro')
time.sleep(5)


# 2 - Manipulando elementos
botao1 = browser.find_element(By.ID, 'onetrust-accept-btn-handler')
botao1.send_keys(Keys.ENTER)

# botao2 = browser.find_element(By.CLASS_NAME, 'financeWatchlistSuggestion_dismiss-DS-EntryPoint1-2')
# botao2.send_keys(Keys.ENTER)

elem_pesq = browser.find_element(By.CLASS_NAME, 'autoSuggest_commonv2-DS-EntryPoint1-1')
elem_pesq.send_keys('petr4')
time.sleep(5)
lupa = browser.find_element(By.XPATH, '//span[@class="searchIconBox_commonv2-DS-EntryPoint1-1"]')
lupa.send_keys(Keys.ENTER)
time.sleep(5) # O PROBLEMA É PEDIR PARA AQUELA LUPA PESQUISAR
# print(lupa.text)
# lupa.send_keys(Keys.ENTER)
# time.sleep(10)




# 3 - buscando elementos