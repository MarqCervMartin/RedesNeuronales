#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:55:23 2019

@author: mar
"""

import numpy as np
import pandas as pd


class MyNeuron:
    #entrenamiento perceptron
    def training(self,X,Y):
        #X matriz numpy Y vector de numpy
        #inicializar w con valores pseudo-aleatorios
        self.W = np.random.random((X.shape[1]+1,1))
        X=np.append(np.ones((X.shape[0],1)),X,axis=1)
        #Nota: Dimensiones de w son el numero de columnas de x+1
        #-----------------------
        for j in range(1,21):
            i=0
            for x in X:
                if np.dot(self.W.T,x) > 0:
                    y=1
                else:
                    y=0
            self.W=self.W+(Y[i]-y)*x.reshape(3,1)
            i=i+1
                
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
    #w=np.array([-6,-1])
    #constructor
    def __init__(self,funcActivation):
        self.funcAct = funcActivation
    #predice si esta aprovado o no
    def predic(self,x):
        x=np.append(1,x)
        y=np.dot(self.W.T,x.reshape(self.W.shape[0])) #producto interno entre w y x
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
         
    #transforma a 0 o 1
    def transformPredictions(self,Y):
        if self.funcAct=='Heaviside':
            idxNeg = Y ==-1
            Y[idxNeg]=0
        elif self.funcAct=='tanh':
            idxPos = Y >=0
            idxNeg = Y <0
            Y[idxPos] = 1
            Y[idxNeg] = 0            
        else:#sigmoid
            idxPos = Y >=0.5
            idxNeg = Y < 0.5
            Y[idxPos] = 1
            Y[idxNeg] = 0  
        return Y
    
clf=MyNeuron("tanh")
datos = pd.read_csv('training.csv')
X = datos.iloc[:,[0,1]]
Y = datos.iloc[:,2]
clf.training(X,Y)

prueba = pd.read_csv('test.csv')
XT = prueba.iloc[:,[0,1]]
YT= prueba.iloc[:,2]
YP = []   

import matplotlib.pyplot as plt
idxPos = YT == 1
idxNeg = YT == 0
Xgraf = XT[idxPos]

plt.plot(Xgraf.iloc[:,0],Xgraf.iloc[:,1],'bo')

Xgraf = XT[idxNeg]
plt.plot(Xgraf.iloc[:,0],Xgraf.iloc[:,1],'ro')
plt.title('TEST')
plt.show()

#conjuntos de datos de entrenamiento
idxPos = Y == 1
idxNeg = Y == 0
Xgraf = X[idxPos]
plt.plot(Xgraf.iloc[:,0],Xgraf.iloc[:,1],'bo')
Xgraf = X[idxNeg]
plt.plot(Xgraf.iloc[:,0],Xgraf.iloc[:,1],'ro')
plt.title('TRAINING')
plt.show()

for i in range (0,XT.shape[0]):
    p=np.array(XT.iloc[1,:])
    YP.append(clf.predic(p))
    
#calculo de la matriz de confusion
#convertir las predicciones en clases
YP = clf.transformPredictions(YP)
YT = np.array(YT)
YT = YT.reshape(YT.shape[0],1)
a = np.sum(np.logical_and(YP==0,YT==0))
b = np.sum(np.logical_and(YP==1,YT==0))
c = np.sum(np.logical_and(YP==0,YT==1))
d = np.sum(np.logical_and(YP==1,YT==1))

cm = np.array([a,b,c,d]).reshape((2,2))
print(cm)