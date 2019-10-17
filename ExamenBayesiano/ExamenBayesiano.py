#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:25:13 2019

@author: mar
"""

"""
@relation contact-lenses

@attribute age 			{young, pre-presbyopic, presbyopic}
@attribute spectacle-prescrip	{myope, hypermetrope}
@attribute astigmatism		{no, yes}
@attribute tear-prod-rate	{reduced, normal}
@attribute contact-lenses	{soft, hard, none}

@data

"""
import pandas as pd
import numpy as np
import random

#cargamos los datos
datos = pd.read_csv('dataSetBayesiano.csv')
x = datos.iloc[:,range(0,4)]
clases = datos.iloc[:,4]
#Obtenemos los valores del 70% de las instancias para entrenamiento y el 30% para prueba
Entrenamiento = round(clases.size*0.7)
print('Entrenamiento #instancias: ')
print(Entrenamiento)
Prueba = clases.size - Entrenamiento
print('Prueba #instancias: ')
print(Prueba)
#Datos aleatorios   shuffle barajear      
#En la linea 35 y 36 se crea un arreglo aleatorio sin repetir para
#tomar como punto de referencia los indices
baraja = list(range(Entrenamiento))
np.random.shuffle(baraja)

print('Indices de datos')
print(clases)
print('Indices nuevos de todos los datos ')
print(baraja)
#Intercambiar los indices del vector baraja con el de clases para revolver instancias
    for i in range(17):
        datos[i] = baraja[i]

#Probabilidades de clase del Entrenamiento
classNone=0    #contador
classSoft=0
classHard=0
instancias = clases.size
    for i in range(0,clases.size):
        if clases.iloc[i] == 'none':
            classNone+=1
        if clases.iloc[i] =='soft':
            classSoft+=1
        if clases.iloc[i] =='hard':
            classHard+=1

PclassNone = classNone/instancias
PclassSoft  = classSoft/instancias
PclassHard = classHard/instancias
print('Probabilidad None :')
print(PclassNone)
print('Probabilidad Soft :')
print(PclassSoft)
print('Probabilidad Hard :')
print(PclassHard)
#Probabilidades Condicionales
#probabilidad entre actividad y la variable age y la clase contact lenses
age = x.iloc[:,0]
hardYoung=0
hardPrePresbyopic=0
hardPresbyopic=0

softYoung=0
softPrePresbyopic=0
softPresbyopic=0

noneYoung=0
nonePrePresbyopic=0
nonePresbyopic=0
# el for calcula las instancias con v=vi y al mismo tiempo clase =ci
    for i in range(0,clases.size):
        if(clases.iloc[i] == 'hard' and age.iloc[i]=='young'):
            hardYoung += 1
        if(clases.iloc[i] == 'hard' and age.iloc[i]=='pre-presbyopic'):
            hardPrePresbyopic +=1
        if(clases.iloc[i] == 'hard' and age.iloc[i]=='presbyopic'):
            hardPresbyopic+=1
        if(clases.iloc[i] == 'soft' and age.iloc[i]=='young'):
            softYoung+=1
        if(clases.iloc[i] == 'soft' and age.iloc[i]=='pre-presbyopic'):
            softPrePresbyopic+=1  
        if(clases.iloc[i] == 'soft' and age.iloc[i]=='presbyopic'):
            softPresbyopic+=1
        if(clases.iloc[i] == 'none' and age.iloc[i]=='young'):
            noneYoung+=1
        if(clases.iloc[i] == 'none' and age.iloc[i]=='pre-presbyopic'):
            nonePrePresbyopic+=1  
        if(clases.iloc[i] == 'none' and age.iloc[i]=='presbyopic'):
            nonePresbyopic+=1
#Probabilidades condicionales entre age y la clase contect-lenses
hardYoung = hardYoung/classNone
hardPrePresbyopic=hardPrePresbyopic/classSoft
hardPresbyopic=hardPresbyopic/classHard

softYoung=softYoung/classNone
softPrePresbyopic=softPrePresbyopic/classSoft
softPresbyopic=softPresbyopic/classHard

noneYoung=noneYoung/classNone
nonePrePresbyopic=nonePrePresbyopic/classSoft
nonePresbyopic=nonePresbyopic/classHard

#Probabilidades para la variable spectacle-prescrip y la clase contact-lenses
spectacle-prescrip = x.iloc[:,1]

hardMyope=0
hardHypermetrope=0

softMyope=0
softHypermetrope=0

noneMyope=0
noneHypermetrope=0
#-----------------------------------Hasta aqui llegue calculo de las probabilidades condicionales
# el for calcula las instancias con v=vi y al mismo tiempo clase =ci
    for i in range(0,clases.size):
        if(clases.iloc[i] == 'hard' and age.iloc[i]=='myope'):
            hardMyope += 1
        if(clases.iloc[i] == 'hard' and age.iloc[i]=='hypermetrope'):
            hardHypermetrope +=1
        if(clases.iloc[i] == 'soft' and age.iloc[i]=='myope'):
            softMyope+=1
        if(clases.iloc[i] == 'soft' and age.iloc[i]=='hypermetrope'):
            softHypermetrope+=1
        if(clases.iloc[i] == 'none' and age.iloc[i]=='myope'):
            noneMyope+=1  
        if(clases.iloc[i] == 'none' and age.iloc[i]=='hypermetrope'):
            noneHypermetrope+=1
        
#Probabilidades condicionales entre age y la clase contect-lenses
hardMyope = hardMyope/classNone
hardPrePresbyopic=hardPrePresbyopic/classSoft

softYoung=softYoung/classNone
softPrePresbyopic=softPrePresbyopic/classSoft

noneYoung=noneYoung/classNone
nonePrePresbyopic=nonePrePresbyopic/classSoft
