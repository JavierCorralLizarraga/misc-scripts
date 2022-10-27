# -*- coding: utf-8 -*-
from lxml import html
import requests
import numpy as np
import pandas as pd
#%%
url = "http://escolar1.rhon.itam.mx/titulacion/titulados.asp?prog="
with open('progValuesTituladosURL') as f:
    prog = f.readlines()
prog = list(map(lambda x: x.replace("\n", ""), prog))
#print(prog)
urls = []
for i in prog:
    urls.append(url + i)
print(urls)
#%%
xpathA = '//tr//td'
page = requests.get(urls[0])
tree = html.fromstring(page.content) 
titu = tree.xpath(xpathA)
titu = list(map(lambda x: x.text_content(), titu))
titu = titu[3:]
titu = list(zip(*[iter(titu)]*2))
df = pd.DataFrame(titu, columns = ['Nombre', 'Año de Graduacion'])
print(df)
#%%
xpathT = "//center"
lics = []
for i in urls:
     page = requests.get(i)
     tree = html.fromstring(page.content) 
     TT = tree.xpath(xpathT)
     TT = list(map(lambda x: x.text_content(), TT))
     TT = TT[1]
     lics.append(TT)
print(lics) 



