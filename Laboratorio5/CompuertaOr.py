#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:35:59 2019

@author: mar
"""
import matplotlib.pyplot as plt
import numpy as np

class MyNeuron:
    #VAriable w global
    WG=0
    xTestPredic=0
    
    #entrenamiento perceptron
    def training(self,X,Y):
        #inicializar w con valores pseudo-aleatorios
        w = np.random.rand(3)
        #Nota: Dimensiones de w son el numero de columnas de x+1
        #-----------------------
        #Paso 2 : Agregar una columna de unos a la matriz x
        X=np.append(np.ones((X.shape[0],1)),X,axis=1)

        #Antes de modificar w guardamos para impresión
        wInicial = w
        XN = X.shape[0] #40
        #Algoritmo perceptron
        for i in range(1,21):
            for j in range(XN):
                if np.dot(w,X[j]) >= 0:
                    y=1
                else:
                    y=0
                w=w+(Y[j]-y)*X[j]
        #guardamos w modificada en wG para despues utilizarla en algoritmo predictivo
        self.WG=w             
        #impersión de resultados
        print("\n\n")
        print("w Inicial: "+str(wInicial))
        print("w Final: "+str(w))
        #graficación de vectores
        plt.plot(wInicial,'.-')
        plt.plot(w,'.-')
        print("\n\n")
        print('Linea azul W Inicial')
        print('Linea naranja W Final aplicando algoritmo')
        
        
    #predice si esta aprovado o no
    def predic(self,i,xTest):
        #calcular y la salida de la prediccion
        y=np.dot(self.WG,xTest[i]) #producto interno entre w y x
        #clasificación
        if self.funcAct=="Heaviside":
            return self.heaviside(y)
        if self.funcAct=="tanh":
            return self.tanh(y)
        if self.funcAct=="sigmoid":
            return self.sigmoid(y)
    
    def comparar(self,XT,Predicciones):
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        #contar true positive, true negative, false negative, false positive
        for i in range(XT.shape[0]):
            if XT[i] ==1 and Predicciones[i]==1:
                TP +=1
            if XT[i] ==0 and Predicciones[i]==0:
                TN +=1
            if XT[i] ==1 and Predicciones[i]==0:
                FN +=1
            if XT[i] ==0 and Predicciones[i]==1:
                FP +=1
        print("\n\nTP = "+str(TP)+"\nTN = "+str(TN)+"\nFP = "+str(FP)+"\nFN = "+str(FN))
        print("\nMatrix Confussion")
        MatrixConfussion = np.array([TP,TN,FP,FN])
        print(MatrixConfussion.reshape(2,2))
        #calculo de Precisión de clasificación
        ClassificationAccuary = ( (TP+TN)/(TP+TN+FN+FP) )*100
        print("\nPrecisión de clasificación: "+str(ClassificationAccuary)+" %")
        
        #calculo de Presición
        Presicion = TP/(TP+FP)*100
        print("Precisión : "+str(Presicion)+" %")   
        
        #calculo de Presición
        Recall = TP/(TP+FN)*100
        print("Recall : "+str(Recall)+" %")  
        
        #calculo de F-Score
        FScore = 2*( (Presicion*Recall)/(Presicion+Recall) )
        print("F-Score : "+str(FScore))
        
    def __init__(self,funcActivation):
        self.funcAct = funcActivation
        
    def heaviside(self,x):
        if x>=0:
            return 1
        else:
            return -1
    def tanh(self,x):
        return np.sinh(x)/np.cosh(x)
    def sigmoid(self,x):
        return  1/(1+np.exp(-x))
    
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
    
    
clf = MyNeuron("tanh")
#Entradas OR
TotalElementos = 10
ceros = np.random.uniform(0,0.4,TotalElementos)
unos = np.random.uniform(0.75,0.9,TotalElementos)
numRenglones = ceros.shape[0]*4
#Conjunto de datos entrenamiento
X = np.append(ceros,ceros)
X = np.append(X,unos)
X = np.append(X,unos)
X = np.append(X,ceros)
X = np.append(X,unos)
X = np.append(X,ceros)
X = np.append(X,unos)
X = X.reshape(numRenglones,2,order=True)


#Clases para Or
YOR = np.zeros([TotalElementos,1])
YOR = np.append(YOR,np.ones([TotalElementos*3,1]))
YOR.reshape(numRenglones,1)


clf.training(X,YOR)

#conjuntos de datos de prueba 20 elementos
cerosTest =  np.zeros(5)
unosTest = np.ones(5)
#Conjunto de datos para compuerta Or
XT = np.append(cerosTest,cerosTest)
XT = np.append(XT,unosTest)
XT = np.append(XT,unosTest)
XT = np.append(XT,cerosTest)
XT = np.append(XT,unosTest)
XT = np.append(XT,cerosTest)
XT = np.append(XT,unosTest)
XT = XT.reshape(20,2,order=True)
#clase para compuerta Or
YT = np.zeros(5)
YT = np.append(YT,np.ones(15))
YT.reshape(YT.size,1)

XT=np.append(np.ones((XT.shape[0],1)),XT,axis=1)
        
Predicciones = []
for i in range(XT.shape[0]):
    Predicciones.append(clf.predic(i,XT))
Predicciones = np.array(Predicciones)
#impresión
print("\n\n")
for i in range(XT.shape[0]):
    print("Indice " +str(i) +" prediccion " +str(Predicciones[i]))
    
Predicciones = clf.transformPredictions(Predicciones)

#Impresión en el método de los calculos Clasificación precisión, precisión,recall y F-score
clf.comparar(YT,Predicciones)
