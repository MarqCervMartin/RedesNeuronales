#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:16:19 2019
Naive Bayes
@author: mar
"""
import pandas as pd
import numpy as np
dataset = pd.read_csv("dataset1.csv")
##dataset.iloc[]
dataset.iloc[:,0]
#otra forma es
dataset.loc[:,'clima']
#pd.read_csv( para saber como leer los dataset
#calcular probabilidad de clases
clases = dataset.iloc[:,2] #clases solo vale todos los valores de la columna 2
np.sum(clases == 'Go-out')/clases.size
np.sum(clases == 'Stay-home')/clases.size
#probabilidad condicional
np.sum([dataset.iloc[:,0] == 'Sunny'] and [clases=='Go-out'])
