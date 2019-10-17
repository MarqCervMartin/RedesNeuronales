# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


lista1=[8,7,4]
import numpy as np
np.array(lista1) #crear un arreglo de numpy a partir de una lista
np.arange(6)
v1 = np.arange(4)
v1.shape #dimensiones del arreglo
type(v1)#tipo de dato
v1.size#numero de elementos

v2 = np.zeros((4,1))
v3 = np.ones((4,1))
print(v2)
print(v3)

v4 = np.full((4,1),5)#crea un arreglo con un valor dado
print(v4)
v5 = 15*np.random.random((4,1))
print(v5)
sigma2=0.8#Desviacion normal probabilidad
mu=7
v6 = np.sqrt(sigma2)*np.random.randn(1,5)+mu
print(v6)
suma = np.add(v3,v4)#sumar matrices con la ayuda de la tarjeta trafica
print(suma)
resta = np.subtract(v4,v3)
producto = np.multiply(v3,v4)
productoEscalar = np.divide(v4,v3)








