#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:14:11 2019

@author: Martin Marquez Cervantes
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
        print("w Inicial: "+str(wInicial))
        print("w Final: "+str(w))
        #graficación de vectores
        plt.plot(wInicial,'.-')
        plt.plot(w,'.-')
        print('Linea azul W Inicial')
        print('Linea naranja W Final aplicando algoritmo')
        
        
    #predice si esta aprovado o no
    def predic(self,i,xTest):
        #calcular y la salida de la prediccion
        y=np.dot(self.WG,xTest[i]) #producto interno entre w y x
        #clasificación
        if y>=0:
            return 1
        else:
            return 0
        #return  1/(1+np.exp(-y))
    
    def comparar(self,ClaseTest,Predicciones):
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        #contar true positive, true negative, false negative, false positive
        for i in range(ClaseTest.shape[0]):
            if ClaseTest[i] ==1 and Predicciones[i]==1:
                TP +=1
            if ClaseTest[i] ==0 and Predicciones[i]==0:
                TN +=1
            if ClaseTest[i] ==1 and Predicciones[i]==0:
                FN +=1
            if ClaseTest[i] ==0 and Predicciones[i]==1:
                FP +=1
        print("\n\nTP = "+str(TP)+"\nTN = "+str(TN)+"\nFP = "+str(FP)+"\nFN = "+str(FN))
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
        
        
        
clf = MyNeuron()
#Entradas
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

Y = np.zeros([TotalElementos*3,1])
Y = np.append(Y,np.ones([TotalElementos,1]))
Y.reshape(numRenglones,1)

clf.training(X,Y)

#conjuntos de datos de prueba
cerosTest =  np.zeros(5)
unosTest = np.ones(5)
#Conjunto de datos
XT = np.append(cerosTest,cerosTest)
XT = np.append(XT,unosTest)
XT = np.append(XT,unosTest)
XT = np.append(XT,cerosTest)
XT = np.append(XT,unosTest)
XT = np.append(XT,cerosTest)
XT = np.append(XT,unosTest)
XT = XT.reshape(20,2,order=True)
YT = np.zeros(15)
YT = np.append(YT,np.ones(5))
YT.reshape(YT.size,1)

XT=np.append(np.ones((XT.shape[0],1)),XT,axis=1)
        
Predicciones = []
for i in range(XT.shape[0]):
    Predicciones.append(clf.predic(i,XT))
Predicciones = np.array(Predicciones)



















