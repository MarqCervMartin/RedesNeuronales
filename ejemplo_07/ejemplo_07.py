#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:43:48 2019

@author: mar
"""

from MyKnn import MyKnn
import pandas as pd
import numpy as np
K=3
print("Escriba alguna distancia:\n1.-euclidean\n2.-manhattan\n3.-cosine\n")
distance = input("")
if distance=='euclidean' or distance == 'manhattan' or distance == 'cosine':
    nuevo_dato = np.array([0,0]) #aqui posiciono el nuevo dato [2.5,4]
    datos = pd.read_csv('datasetKnn.csv')
    X = datos.iloc[:,range(0,2)]
    clases = datos.iloc[:,2]
    clasificador = MyKnn()
    pred = clasificador.clasify(X,clases,nuevo_dato,K,distance)
    print("La prediccion es: ")
    print(pred)
else:
    print("Introduce una distancia valida")
    