#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:16:01 2019

@author: mar
"""

import pandas as pd
import numpy as np

"""
@relation weather.symbolic
@attribute outlook {sunny, overcast, rainy}
@attribute temperature {hot, mild, cool}
@attribute humidity {high, normal}
@attribute windy {TRUE, FALSE}
@attribute play {yes, no}
@data

"""
#cargamos los datos
datos = pd.read_csv('DataSetBayesiano.csv')
x = datos.iloc[:,range(0,4)]
clases = datos.iloc[:,4]


#Probabilidades de clase
classYes=0    #contador
classNo=0
instancias = clases.size
    for i in range(0,clases.size):
        if clases.iloc[i] == 'yes':
            classYes+=1
        elif clases.iloc[i] =='no':
            classNo+=1

PclassYes = classYes/instancias
PclassNo  = classNo/instancias

print(PclassYes)
print(PclassNo)

#Probabilidades Condicionales
#probabilidad entre actividad y la variable outlook 
outlook = x.iloc[:,0]
yesSunny=0
noSunny=0
yesOvercast=0
noOvercast=0
yesRainy=0
noRainy=0
m=0
    for i in range(0,clases.size):
        if(clases.iloc[i] == 'yes' and outlook.iloc[i]=='sunny'):
            yesSunny += 1
        if(clases.iloc[i] == 'no' and outlook.iloc[i]=='sunny'):
            noSunny +=1
        if(clases.iloc[i] == 'yes' and outlook.iloc[i]=='overcast'):
            yesOvercast+=1
        if(clases.iloc[i] == 'no' and outlook.iloc[i]=='overcast'):
            noOvercast+=1
        if(clases.iloc[i] == 'yes' and outlook.iloc[i]=='rainy'):
            yesRainy+=1  
        if(clases.iloc[i] == 'no' and outlook.iloc[i]=='rainy'):
            noRainy+=1

yesSunny = yesSunny/classYes
noSunny=noSunny/classNo
yesOvercast=yesOvercast/classYes
noOvercast=noOvercast/classNo
yesRainy=yesRainy/classYes
noRainy=noRainy/classNo
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            