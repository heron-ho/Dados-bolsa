from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Utilizando o webdriver

browser = webdriver.Chrome()
browser.get('https://www.sustainalytics.com/esg-rating/cemig-gera-o-e-transmiss-o-sa/2000158958')
time.sleep(5)

# 1 - eliminando cookies

cookie = browser.find_element(By.ID, 'hs-eu-confirmation-button')
cookie.send_keys(Keys.ENTER)
time.sleep(4)

# indo para o input do site
elem_pesq = browser.find_element(By.ID, 'searchInput')
elem_pesq.send_keys('petr4') #nome das empresas quando iterar vai aqui.
time.sleep(4)

item_empresa = browser.find_element(By.CLASS_NAME, 'search-link js-fix-path') # corrigir aqui e tentar denovo!!!!
item_empresa.send_keys(Keys.DOWN)
time.sleep(5)

# elem_selec = browser.find_element(By.XPATH, '//*[@id="searchResults"]/div/div/div/a')
# elem_selec.send_keys(Keys.ENTER)
# time.sleep(4)