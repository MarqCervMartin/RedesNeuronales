#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:21:42 2019

@author: Martín Márquez Cervantes
Uso de pytorch descargar pytorch en: https://pytorch.org/
Actividad : 
    -Como multiplicar vectores en pytorch
    -Generar números aleatorios
    -Métodos view,reshape,nm
    
COntiene caracteristicas de numpy, enfocada al machine learning
desarrollada por los developers de facebooks
"""
import torch


def funcAct(x):
    return 1/(1+torch.exp(-x))

#Caracteristicas entradas
features  = torch.randn((1,5))
#un tensor es un array que puede multidimensionar

#Pesos sinapticos
W = torch.randn_like(features)
#reshape y resize tienen diferencias en el movimiento de los arrays en memoria
W.view(5,1)
#W.T
#randn likes hace un vector con las mismas dimensiones en este caso de features

#bias
bias = torch.randn(1,1)
x = funcAct(torch.sum(W*features+bias))
print(x)