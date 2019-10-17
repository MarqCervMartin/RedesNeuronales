#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:53:57 2019

@author: Martin Marquez Cervantes ICO CU UAEM Zumpango
"""
#En el plano 2D dado diez tuplas(coordenadas x,y) generados aleatoriamente
#Ingresando una nueva tupla calcula su distancia entre cada una e imprime
#las coordenadas de las tres primeras distancias menoras K=3
import numpy as np
import matplotlib.pyplot as plt
#creacion de los arreglos numpy
B = np.random.random((10,2))
pr = np.random.random((2,1))

plt.plot(pr[0],pr[1],'bo')
plt.plot(B[:,0], B[:,1], 'ro')
plt.axis([-1,1,-1,1])
plt.grid(True)
plt.show
#impresión de los puntos
#Rayones xD Hasta aqui termina ejemplo_05
#k=3 impresion de las coordenadas mas cercanas

"""
k = np.zeros((3,2))
k = np.append(k,(1,2))
k = np.append(k,(3,4))
k = k.reshape(-1,2)
"""
#calculo de las distancias y acumulacion en un arreglo distancias numpy
arrayDistancias = np.zeros((10))
print("Distancias")
for i in range(0,10):
    d = np.sqrt( np.sum(np.power(np.subtract(B[i],pr),2.0) ) )
    print(d)
    arrayDistancias[i] = d
#obtener las 3 distancias menores
#con numpy argmin devuelve los indices de los valores minimos
# amin devuelve el valor minimo
#lo siwnto profe no pude con el algoritmo de 3 busquedas secuenciales xD le dejo lo que pude con funciones de numpy
print('\n\n Coordenadas con distancias minimas k=3')
for i in range(1,4):
    indexMin=np.argmin(arrayDistancias)
    print(B[indexMin])
    arrayDistancias[indexMin]=2

print("\nMatriz B\n")
print(B)

#argsort hacia toda la chamba
