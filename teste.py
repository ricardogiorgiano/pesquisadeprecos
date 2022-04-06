from urllib.request import urlopen
from urllib.request import HTTPErrorProcessor
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from itertools import count

tag_pesquisa = "7899882306569"


def price_spider():
	
	
		html = urlopen("https://www.amazon.com.br/s?k=" % (tag_pesquisa))
		bsObj = BeautifulSoup(html,"html.parser")
		
		nameList = bsObj.findAll("a",{"class":"history-item"})
		priceList = bsObj.findAll("span",{"class":"value"})

		for name in nameList:
			print(name.get_text())

		for price in priceList:
			print(price.get_text())
	

	







