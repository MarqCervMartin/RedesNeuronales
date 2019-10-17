#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:24:41 2019

@author: mar
"""
import numpy as np
pa = np.array([-2,-2])
pb = np.array([1,3])
pc = np.array([4,3])
pr = np.array([-3,-1])
#para elevar al cuadrado en python  = **2 doble asterisco y la potencia
resta = np.subtract(pa,pr)  #paso a paso
restaCuadrado = np.power(resta,2.0)
sumatoria = np.sum(restaCuadrado)
distancia = np.sqrt(sumatoria)
distanciaAR = np.sqrt( np.sum(np.power(np.subtract(pa,pr),2.0) ) ) #un solo paso
distanciaBR = np.sqrt( np.sum(np.power(np.subtract(pb,pr),2.0) ) )
distanciaCR = np.sqrt( np.sum(np.power(np.subtract(pc,pr),2.0) ) )

miVector = np.array([1,2,3,4,5,6,7,8,9])
A = miVector.reshape(3,3) #cambia a matriz
B = pa # la matriz B comienza con pa
B = np.append(B,pb)#se le agrega
B = np.append(B,pc)#pb y pc
B =B.reshape(-1,2)#se cambia a matriz de dos columnas
pr = np.array([-3,-1])
aux = 0
for i in range(0,3):
    d = np.sqrt( np.sum(np.power(np.subtract(B[i],pr),2.0) ) )
    print(d)      
    if i==0:
        distMin = d
        indiceMin = i
    if d<distMin:
        distMin = d
        indiceMin = i
        
print(B[indiceMin, :])
import matplotlib.pyplot as plt
plt.plot(B[:,0], B[:,1], 'ro')
plt.plot(pr[0],pr[1],'bo')
plt.axis([-5,5,-4,6])
plt.grid(True)
plt.show
    
    
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
