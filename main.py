from itertools import count
from mysqlx import Column, Row
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#automatização web
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

baseDados = "basededados.xlsx"


UrlLA = "https://www.americanas.com.br/busca/"
UrlMA = "https://www.magazineluiza.com.br/busca/"
UrlGO = "https://www.google.com.br/search?tbm=shop&hl=pt-BR&psb=1&ved=2ahUKEwiW_9WUsOv2AhWRUEgAHUAeAQ0Qu-kFegQIABAK&q="



df = pd.read_excel(baseDados)
df.count



for lin in range(len(df)):
    
    linkAM = ("")
    UrlAM = "https://www.amazon.com.br/s?k="
    chrome = webdriver.Chrome() #Carrega o Chrome
    chrome.get(UrlAM,{lin}) #Entra na URL    
    




#for index,row in df.iterrows():
#    print("Index: "+ str(index) + " Na linha tem o produto: " + row["Descrição do Produto"])
#    chrome = webdriver.Chrome() #Carrega o Chrome

#    chrome.quit #Sai do Chrome













