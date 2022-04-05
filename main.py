from itertools import count
from mysqlx import Column, Row
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#automatização web
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

baseDados = pd.read_excel(r'basededados.xlsx')
baseDados = baseDados.fillna('-')

print(baseDados)

def transformar_texto(texto):
    return float(texto.replace('R$', '').replace('.', '').replace(',', '.'))

driver = webdriver.Chrome()
#driver.set_window_position(-10000,0)

for i, linha in baseDados.iterrows():
    
    UrlAM = driver.get("https://www.amazon.com.br/s?k=" + str(linha['EAN']))
    #linkAM = 


baseDados.loc[i,'LINK AMAZON'] = UrlAM


baseDados.to_excel('basededados.xlsx')


#UrlLA = "https://www.americanas.com.br/busca/"
#UrlMA = "https://www.magazineluiza.com.br/busca/"
#UrlGO = "https://www.google.com.br/search?tbm=shop&hl=pt-BR&psb=1&ved=2ahUKEwiW_9WUsOv2AhWRUEgAHUAeAQ0Qu-kFegQIABAK&q="






#for index,row in df.iterrows():
#    print("Index: "+ str(index) + " Na linha tem o produto: " + row["Descrição do Produto"])
#    chrome = webdriver.Chrome() #Carrega o Chrome

#    chrome.quit #Sai do Chrome













