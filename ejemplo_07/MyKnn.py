u#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:28:33 2019

@author: mar
"""
import numpy as np

datos = np.random.rand(4,2)
nuevo_dato = np.random.rand(1,2)

#para declarar clases:
class MyKnn:
    #datos es una matriz de numpy
    #nuevo_dato es un vector de numpy
    #K es el numero de vecinos mas cercanos
    #distance es una cadena indicando la distancia a usar: euclidian, manhatan ,mahalanobbis,cosine,etc
    #Clases contiene las etiquetas de los datos
    def clasify(self,datos,clases,nuevo_dato,K,distance):#declaro funciones self = this
        N = datos.shape[0]
        x = nuevo_dato
        distancias = []
        #calcula las distancias
        for m in range(0,N):
            y = datos.iloc[m,:]
            if distance =="euclidean":
                self.euclidianDistance(x,y)
                distancias.append(self.euclidianDistance(x,y)) #acumula las distancias
            if distance == "manhattan":
                #self.manhattanDistance(x,y)
                distancias.append(self.manhattanDistance(x,y))
            if distance == "cosine":
                distancias.append(self.cosineSimilarity(x,y))
                
                
        indices = np.argsort(distancias)
        #think about this para más clases en este caso es de dos 0,1
        uno = 0
        cero=0
        for i in range(0,K):
            j = indices[i]
            if clases[j] ==0:
                cero = cero+1
            elif clases[j] ==1:
                uno = uno+1
        if cero>uno:
            return 0
        if uno>cero:
            return 1
                
        
    #x y Y son vectores numpy
    def euclidianDistance(self,x,y):
        return np.sqrt(np.sum(np.power(np.subtract(x,y),2.0)))
    
    def manhattanDistance(self,x,y):
        return np.sum(np.absolute(np.subtract(x,y))) #implementacion del calculo distancia manhattan
    
    def cosineSimilarity(self,x,y):
        return 1-np.divide(np.sum(np.multiply(x,y)),np.sqrt(np.multiply(np.sum(np.power(x,2.0)),np.sum(np.power(y,2.0)))))