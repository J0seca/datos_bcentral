#-*- coding: utf-8 -*-
#Indices banco central Chile

import urllib
from urllib import request
from bs4 import BeautifulSoup

source = urllib.request.urlopen("https://si3.bcentral.cl/Indicadoressiete/secure/Indicadoresdiarios.aspx")
soup = BeautifulSoup(source)

print("Indicadores del banco central:\n"+25*"-")

print("Unidad de fomento (UF): " + soup.find(id="lblValor1_1").get_text() + " CLP")
print("Dólar Observado: " + soup.find(id="lblValor1_3").get_text() + " CLP")
print("Onza de Oro: " + soup.find(id="lblValor2_3").get_text() + " USD")
print("Onza de Plata: " + soup.find(id="lblValor2_4").get_text() + " USD")
print("Libra de Cobre: " + soup.find(id="lblValor2_5").get_text() + " USD")
print(25*"-")
