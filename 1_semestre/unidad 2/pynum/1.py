#numpy es una libreira especializada en el calcilo numérico y el analisis de datos
#incorpora arrays multidimencionales
#los arrays de numpy son más eficientes que las listas de python para operaciones matemáticas

import numpy as np

                    #CREACION DE ARRAYS

a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]) #array 3x5
zero=np.zeros((3,4)) #array de ceros de 3 filas y 4 columnas
ones=np.ones((2,5))  #array de unos de 2 filas y


                    #PROPIEDADES DE LOS ARRAYS
                    
a.ndim  #número de dimensiones
a.shape #devuelve una tupla con las dimensiones del array
a.size  #número de elementos del array
a.dtype #tipo de datos de los elementos del array

                    #INDICES
                    
elemento=a[2,1]      #acceder al tercer elemento 
#a diferecnai de las listas a[2][1] no funciona

                #ALGEBRA VECTORIAL

pelota = np.array([2,3])
modulo = pelota.norm()  #me da la magnitud 
angulo = np.arctan(pelota[1], pelota[0]) #ángulo en radianes


