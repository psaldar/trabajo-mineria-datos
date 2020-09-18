# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:16:42 2020

@author: Pablo Saldarriaga
"""
### Este script toma el archivo de metadata de los productos de amazon
### disponibles en http://jmcauley.ucsd.edu/data/amazon/ y extrae las columnas
### relevantes, ademas de guardar los resultados en diferentes archivos CSV
### con una capacidad maxima de 1.5 millones de registros

import os
import json
import gzip
import pandas as pd

count = 0
ids = 0
data = []
res = pd.DataFrame()
with gzip.open(r"D:\Downloads\All_Amazon_Meta.json.gz") as f:
    for l in f:     
        data.append(json.loads(l.strip()))
        count = count + 1
        if count % 1500000 == 0:
            ids = ids + 1
            df = pd.DataFrame.from_dict(data)
            df[['asin','price','title','brand','category','description']].to_csv(f'D:/Documents/data/products/products_{ids}.csv', index = False)
            df = pd.DataFrame()
            data = []
            print(count)

ids = ids + 1
df = pd.DataFrame.from_dict(data)
df[['asin','price','title','brand','category','description']].to_csv(f'D:/Documents/data/products/products_{ids}.csv', index = False)
print('Listo')