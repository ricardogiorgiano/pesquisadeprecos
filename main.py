from cgitb import text
from itertools import count
from mysqlx import Column, Row
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select




baseDados = pd.read_excel(r'basededados.xlsx')
baseDados = baseDados.fillna('-')



driver = webdriver.Chrome()

#def transformar_texto(texto):
#    return float(texto.replace('R$', '').replace('.', '').replace(',', '.'))

#driver.set_window_position(-10000,0)

for i, linha in baseDados.iterrows():
    
    #criar link Amazon
    UrlAM = driver.get("https://www.amazon.com.br/s?k=" + str(linha['EAN']))
    driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/h2/a').click()
    linkAM = driver.current_url
    
    precoAM = driver.find_element_by_tag_name('span(95)').text
    baseDados.loc[i,'LINK AMAZON'] = linkAM
    baseDados.loc[i,'precoAM'] = precoAM

    
    
    UrlLA = driver.get("https://www.americanas.com.br/busca/" + str(linha['EAN']))
    driver.find_element_by_xpath('//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]/div[1]/div/div/a').click()
    linkLA = driver.current_url
    baseDados.loc[i,'LINK LA'] = linkLA
    

    #UrlMA = driver.get("https://www.magazineluiza.com.br/busca/" + str(linha#['Descrição do Produto']))
    #driver.find_element_by_xpath('//*[@id="__next"]/div/main/section[4]/div[3]/div/#ul/li[1]/a').click()
    #linkMA = driver.current_url
    #baseDados.loc[i,'LINK MAGALU'] = linkMA
    
    
    baseDados.to_excel('basededados.xlsx',index=False)
    



    
    

    

#baseDados.loc[i,'LINK AMAZON'] = linkAM
#baseDados.loc[i,'LINK LA'] = linkLA


#baseDados.to_excel('basededados.xlsx')


#UrlLA = "https://www.americanas.com.br/busca/"
#UrlMA = "https://www.magazineluiza.com.br/busca/"
#UrlGO = "https://www.google.com.br/search?tbm=shop&hl=pt-BR&psb=1&ved=2ahUKEwiW_9WUsOv2AhWRUEgAHUAeAQ0Qu-kFegQIABAK&q="






#for index,row in df.iterrows():
#    print("Index: "+ str(index) + " Na linha tem o produto: " + row["Descrição do Produto"])
#    chrome = webdriver.Chrome() #Carrega o Chrome

#    chrome.quit #Sai do Chrome













