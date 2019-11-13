#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:34:04 2019

@author: mar
BackPropagacion
"""
#NUmero de entradas = 3
#Numero de salidas = 1
import torch
def funcAct(x):
    return 1/(1+torch.exp(-x))

numberInputs = 3
outputLayer = 1
hiddenLayer  = 2
torch.manual_seed(8)

W1 = torch.randn((numberInputs,hiddenLayer))
W2 = torch.randn((hiddenLayer,numberInputs))
features = torch.randn((1,numberInputs))
y1 = torch.sum(features.view(3,1)*W1,axis=0)

#m = torch.randint(0,4,(2,2))   matriz numero minimo 0,maximo4 y de 2x2
#torch.sum(m,axis=0)            eje de las filas y 1 columnas en axis


yOut = funcAct(torch.sum(y1.view(2,1)*W2))
print(yOut) #salida de la red neuronal ejemplo Part1-Tensor in PyTorch

#rm multiplicacion de matrices
#tensores a numpy
yOut.numpy()  #dtype es un tipo flotante de 32 bytes

#numpy a tensor
import numpy as np 
torch.from_numpy(np.array([1,2,3]))




