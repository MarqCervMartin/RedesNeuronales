#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:20:52 2019

@author: mar
from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)
import torch
torch.cuda.is_available()

Crea	 una	 clase	 en	 Python llamada	 MyForwardNN,	 que	 contenga	 un	 método	
llamado	initNN que	permita	crear	una	red	neuronal	con	la	arquitectura	vista	en	
clases.	
"""
#importamos numpy hasta el momento
import numpy as np
#crear clase MyForwardNN
class MyForwardNN:
    #Funciones de activación
    def heaviside(self,x):
        if x>=0:
            return 1
        else:
            return -1
    def tanh(self,x):
        return np.sinh(x)/np.cosh(x)
    def sigmoid(self,x):
        return  1/(1+np.exp(-x))
    #def __init__():
    #recibe numero de entradas,capas ocultas,numero neuronas en cada capa
    #numero de salidas y funcion de activacion
    """
    b) Dentro	 del	 método,	 se	 deben	 de	 generar	 TODAS	 las	 matrices	 necesarias,	
    inicializándolas	 con	 valores	 pseudoaleatorios	 entre	 -1.0 y	 1.0 con	 una	
    distribución	de	probabilidad	normal.
    """
    #metodo init que construye matrices
    def initNN(self,inputs,HiddenLayer,neurons,outputs,funcActivation):
        #Entradas
        #xInput = np.random.randn(inputs,1)
        #x_Input = np.append(1,x)
        
                            #Crear matrices W
        #lista W que contendra matrices
        W = []
        #for para crear las matrices
        for i in range(HiddenLayer+1):
            #lista de arreglos
            W.append( np.random.rand(neurons[i],inputs+1)*2.0-1.0 )
            W[i].reshape((neurons[i],inputs+1)) 
            #W[i] = np.append(1,W[i])  creo que debo añadir lista de ones
            #W[i].reshape((neurons[i],inputs+1))
            inputs = neurons[i]
        #impresión de matrices
        for i in range(HiddenLayer+1):
            print("\n")
            print("W"+str(i))
            print(W[i])    
        
            
        
clf = MyForwardNN()
#inputs,hiddenlayers,neurons,outputs,funcActivacion
inputs = 2 #Numero de entradas
HiddenLayer = 2 #numero de capas ocultas
neurons = [2,4,3]
outputs = 3
funcActivacion = "Heaviside"
#llamamos al metodo initNN
clf.initNN(inputs,HiddenLayer,neurons,outputs,funcActivacion)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
