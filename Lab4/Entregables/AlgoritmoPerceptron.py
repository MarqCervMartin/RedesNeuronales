#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:44:02 2019

@author: Martin Marquez Cervantes
"""
import matplotlib.pyplot as plt
import pandas as pd
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
        #Crear una matriz del mismo tamaño que las filas 23x1
        xOnes = np.ones(int((X.size)/2)).reshape((23,1))
        #insertarlas en la varible datos en el indice cero
        datos.insert(0,"Ones",xOnes)
        #asignar los nuevos datos a X
        #Xvar=datos.iloc[:,range(0,3)]
        X1 = np.array(datos.iloc[:,range(0,3)])
        #Cambio de formato array pandas a array numpy no me salia por esto ;(
        Y = np.array(Y)
        
        
        """
        Paso3 :for i=1 to N (N vale 20)
                   for cada renglon de x de X
                       calcular WTx
                       if el producto es positivo then 
                           y = 1
                        else
                            y=0
                        W=W+(yi+y)xi
        """
        #Antes de modificar w guardamos para impresión
        wInicial = w
        XN = int(X.size/3) #23
        #Algoritmo perceptron
        for i in range(1,21):
            for j in range(XN):
                if np.dot(w,X1[j]) >= 0:
                    y=1
                else:
                    y=0
                w=w+(Y[j]-y)*X1[j]
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
            return 1 #Aprobado
        else:
            return 0 #No aprobado
    
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
        
#Instancia de la clase MyNeuron    
clf = MyNeuron()
#carga de la data training
datos = pd.read_csv("training.csv")
#X matriz pandas Y vector de pandas
X=datos.iloc[:,range(0,2)]
Y=datos.iloc[:,range(2,3)]
#método
clf.training(X,Y)
#-------------------------------------------------------------------------
#carga de la data test
datosTest = pd.read_csv("test.csv")
#Crear una matriz del mismo tamaño que las filas con nuevo metodo shape[0]
XTestOnes = np.ones(datosTest.shape[0]).reshape((datosTest.shape[0],1))

#insertarlas en la varible datos en el indice cero
datosTest.insert(0,"Ones",XTestOnes)

#asignar los nuevos datos a X(X1,X2,X3)
xTest = np.array(datosTest.iloc[:,range(0,3)])

#for de 0 hasta tamaño de fila de los datos shape[0], mandamos indice a método predic
#llenamos el array Predicción
Predicciones = []
for i in range(datosTest.shape[0]):
    Predicciones.append(clf.predic(i,xTest))
Predicciones = np.array(Predicciones)
#impresión
for i in range(datosTest.shape[0]):
    print("Indice " +str(i) +" prediccion " +str(Predicciones[i]))
#COmpara y calcula la tabla de confusión
ClaseTest = np.array(datosTest.iloc[:,3])
#Impresión en el método de los calculos Clasificación precisión, precisión,recall y F-score
clf.comparar(ClaseTest,Predicciones)