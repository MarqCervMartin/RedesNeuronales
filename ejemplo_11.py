#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:24:58 2019

@author: Martin MArquez Cervantes

Ejemplo funcionamiento de una red neuronal
Entradas: 3
Capas ocultas 
    primera:2
    segunda:4
Salidas: 3
Función de activacion logistica
"""
#Arquitectura
import numpy as np
def funcActivacion(x):
    return 1/(1+np.exp(-x))

#x = np.array([.5,1]) #Entradas ejemplo
x = np.random.rand(2,1)
x_ext = np.append(1,x)
W1 = 2.1*np.random.random([2,3])
f = funcActivacion(np.dot(W1,x_ext)) #dot producto entre matrices
f1 = np.append(1,f)

W2 = np.random.randn(4,3)#randn numeros negativos
f = funcActivacion(np.dot(W2,f1))
f2 = np.append(1,f)
#print(f2.reshape(f2.size,1))
W3 = np.random.randn(3,5)
y = funcActivacion(np.dot(W3,f2))
print(y)

