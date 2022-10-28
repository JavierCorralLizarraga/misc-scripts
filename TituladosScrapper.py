# -*- coding: utf-8 -*-
from lxml import html
import requests
import numpy as np
import pandas as pd
from pandasql import sqldf
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
# xpathA = '//tr//td'
# page = requests.get(urls[0])
# tree = html.fromstring(page.content) 
# titu = tree.xpath(xpathA)
# titu = list(map(lambda x: x.text_content(), titu))
# titu = titu[3:]
# titu = list(zip(*[iter(titu)]*2))
# df = pd.DataFrame(titu, columns = ['Nombre', 'Año de Graduacion'])
#print(df)
#%%
xpathT = "//center"
xpathA = '//tr//td'
lics = {}
for i in urls:
     page = requests.get(i)
     tree = html.fromstring(page.content) 
     titu = tree.xpath(xpathA)
     titu = list(map(lambda x: x.text_content(), titu))
     titu = titu[3:]
     titu = list(zip(*[iter(titu)]*2))
     df = pd.DataFrame(titu, columns = ['Nombre', 'Año_Grad'])
     TT = tree.xpath(xpathT)
     TT = list(map(lambda x: x.text_content(), TT))
     TT = TT[1]
     lics[TT] = df
#print(lics)      
#%%
lic = list(lics.keys())
#print(lic[-3])
dfA = lics[lic[0]]
#print(dfA)
dfM = lics[lic[-3]]
#print(dfM)
#query = "select * from df order by Año_Grad desc limit 1"
query = """select count(*) as Matematicas, Año_Grad 
            from dfM 
            group by Año_Grad
"""
query2 = """select count(*) as Matematicas, Año_Grad 
            from dfA 
            group by Año_Grad
""" 
#['Actuaria', 'Matematicas']
sqldf(query).plot(x='Año_Grad', y='Matematicas', title='Titulados ITAM por año')
#print(sqldf(query))




