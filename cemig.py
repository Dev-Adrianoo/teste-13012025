from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import signal

chrome_options = Options()
chrome_options.add_argument("--headless") 
service = Service("/usr/bin/chromedriver")  
web = webdriver.Chrome(service=service, options=chrome_options)

web.get("https://www.cemig.com.br/atendimento/valores-de-tarifas-e-servicos/")


wait = WebDriverWait(web, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr[1]/td[4]')))

def get_tarifa_bandeira(xpath):
    try:
        elemento = web.find_element(By.XPATH, xpath)
        return elemento.text
    except Exception as e:
        print(f"Erro ao buscar a tarifa com o XPath {xpath}: {e}")
        return None

tarifa_residencial_bandeira_vermelha1 = get_tarifa_bandeira('//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr[1]/td[4]')
tarifa_residencial_bandeira_verde = get_tarifa_bandeira('//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr[1]/td[2]')
tarifa_residencial_bandeira_amarela = get_tarifa_bandeira('//*[@id="main-content"]/section[8]/div/div/div/table/tbody/tr[1]/td[3]')

tarifa_comercial_industrial_bandeira_verde = get_tarifa_bandeira('//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr[1]/td[2]')
tarifa_comercial_industrial_bandeira_amarela = get_tarifa_bandeira('//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr[1]/td[3]')
tarifa_comercial_industrial_bandeira_vermelha1 = get_tarifa_bandeira('//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr[1]/td[4]')
tarifa_comercial_industrial_bandeira_vermelha2 = get_tarifa_bandeira('//*[@id="main-content"]/section[14]/div/div/div/table/tbody/tr[1]/td[5]')


print(f"Tarifa Residencial - Bandeira Vermelha 1: {tarifa_residencial_bandeira_vermelha1}")
print(f"Tarifa Residencial - Bandeira Verde: {tarifa_residencial_bandeira_verde}")
print(f"Tarifa Residencial - Bandeira Amarela: {tarifa_residencial_bandeira_amarela}")

print(f"Tarifa Comercial e Industrial - Bandeira Verde: {tarifa_comercial_industrial_bandeira_verde}")
print(f"Tarifa Comercial e Industrial - Bandeira Amarela: {tarifa_comercial_industrial_bandeira_amarela}")
print(f"Tarifa Comercial e Industrial - Bandeira Vermelha 1: {tarifa_comercial_industrial_bandeira_vermelha1}")
print(f"Tarifa Comercial e Industrial - Bandeira Vermelha 2: {tarifa_comercial_industrial_bandeira_vermelha2}")


try:
    web.quit()
except Exception as e:
    print(f"Erro ao tentar fechar o WebDriver: {e}")
   
    try:
        pid = os.getpid()  
        os.kill(pid, signal.SIGTERM)  
    except Exception as e:
        print(f"Erro ao tentar finalizar o processo: {e}")
