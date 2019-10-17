#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:28:46 2019

@author: mar
"""
#Primer ejemplo con una neurona muy simple

import random
import numpy as np


class MyNeuron:
    #entrenamiento perceptron
    def training(self,X,Y):
        #X matriz numpy Y vector de numpy
        #inicializar w con valores pseudo-aleatorios
        w = random.randrange(-1,1,2)
        #Nota: Dimensiones de w son el numero de columnas de x+1
        #-----------------------
        
        """Paso 2 : Agregar una columna de unos a la matriz x
        Paso3 :for i=1 to N (N vale 20)
                   for cada renglon de x de X
                       calcular WTx
                       if el producto es positivo then 
                           y = 1
                        else
                            y=0
                        W=W+(yi+y)xi
        """
    
    #pesos sinapticos
    w=np.array([-12,2])
    #w=np.array([-6,-1])
    #constructor
    def __init__(self,funcActivation):
        self.funcAct = funcActivation
    #predice si esta aprovado o no
    def predic(self,nuevaCalif):
        x=np.array([1,nuevaCalif])
        y=np.dot(self.w,x) #producto interno entre w y x
        """
        if y>=0:
            return 1 #Aprobado
        else:
            return -1 #No aprobado
        """
        if self.funcAct=="Heaviside":
            return self.heaviside(y)
        if self.funcAct=="tanh":
            return self.tanh(y)
        if self.funcAct=="sigmoid":
            return self.sigmoid(y)
        
    
    def heaviside(self,x):
        if x>=0:
            return 1
        else:
            return -1
    def tanh(self,x):
        return np.sinh(x)/np.cosh(x)
    def sigmoid(self,x):
        return  1/(1+np.exp(-x))
            
        
clf=MyNeuron("Heaviside")
"""
for i in range(0,10):
    print("calificacion " +str(i) +" prediccion " +str(clf.predic(i)))
   """ 
for i in np.linspace(0,10,11):
    print("calificacion " +str(i) +" prediccion " +str(clf.predic(i)))
    
#implementar el algortimo del perceptron simple

        