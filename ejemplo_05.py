import numpy as np
B = np.random.random((10,2))
import matplotlib.pyplot as plt
pr = np.random.random((2,1))

plt.plot(pr[0],pr[1],'bo')
plt.plot(B[:,0], B[:,1], 'ro')
plt.axis([-1,1,-1,1])
plt.grid(True)
plt.show
#Hasta aqui termina ejemplo_05
#k=3 impresion de las coordenadas mas cercanas

"""
k = np.zeros((3,2))
k = np.append(k,(1,2))
k = np.append(k,(3,4))
k = k.reshape(-1,2)
"""

arrayDistancias = np.zeros((10))
print("Distancias")
for i in range(0,10):
    d = np.sqrt( np.sum(np.power(np.subtract(B[i],pr),2.0) ) )
    print(d)
    arrayDistancias[i] = d
#obtener las 3 distancias menores
#con numpy argmin devuelve los indices de los valores minimos
# amin devuelve el valor minimo
#lo siwnto profe no pude con el algoritmo de 3 busquedas secuenciales xD
print('\n\n')
for i in range(1,4):
    indexMin=np.argmin(arrayDistancias)
    print(B[indexMin])
    arrayDistancias[indexMin]=2



"""
for i in range(0,4):
    d1 = np.amin(arrayDistancias)
    indice1 = np.indexmin
    
    
k[0] = B[0]
k[1] = B[1]
k[2] = B[2]

for i in arrayDIstancias:
    if arrayDistancias[i]<
        d1 = arrayDistancias[0]
        
"""
        
    

#Laboratorio dados 10 puntos en el plano y un punto de referencia:
#a)Graficar los puntos con pyplot
#b)Imprimir las coordenadas de los k=3 puntos más cercanos al punto de referencia
#este ejemplo fue de k=1



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