# examen proximo martes 11 de nov

import matplotlib.pyplot as plt
import numpy as np

xpunto = np.array([0, 6])
ypunto = np.array([0, 250])

# plt.plot(xpunto, ypunto)    #grafic dos vectores en 2D

xpuntos = np.array([0, 3,6,8])
ypuntos = np.array([0, 250,100,300])
u= np. array([3,4])
v= np. array([1,2])

x_pos= 0
y_pos= 0
x_direct = 1
y_direct = 1

# plt.scatter(xpuntos, ypuntos)  #scatter hace grafico de dispersion
# plt.fill_between(xpunto, ypunto, color='red', alpha=0.4)    #rellena el area bajo la curva
# plt.bar(xpuntos, ypuntos, width=0.5, color='green', alpha=0.6)  #grafico de barras
# plt.pie([4,3,2,1])

# plt.arrow(0,0,u[0], u[1],head_width=.1, ec='green')
# plt.arrow(0,0,v[0], v[1],head_width=.1, ec='red')

# plt.quiver(0,0,1,1) #para campos vectoriales

#                crear varios grafcicos o o juntar graficas

# fig, ax = plt.subplots(2) #crea dos graficos en una misma figura
# ax[0].plot(xpuntos, ypuntos)
# ax[1].scatter(xpuntos, ypuntos)

#               usar varios graficos en una varias figuras

# fig, (ax1, ax2) = plt.subplots(1,2) #una figura de 1 fila x 2 columnas
# fig.suptitle('Graficos en subplots')
# ax1.plot(xpuntos, ypuntos)
# ax2.plot(xpuntos, -ypuntos)

#              una figura como matris

fig, axs = plt.subplots(2,2) #una figura de 2 filas x 2 columnas
axs[0,0].plot(xpuntos, ypuntos)
axs[0,1].scatter(xpuntos, ypuntos)  
axs[1,0].bar(xpuntos, ypuntos)
axs[1,1].pie([4,3,2,1])

plt.xlavel('energias') # establece titulos

# plt.savefig('mi_grafico.png') #guarda la figura actual

#                 graficar en 3D

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# z = np.linspace(0, 1, 100)
# x = z * np.sin(25 * z)
# y = z * np.cos(25 * z)

# ax.plot3D(x, y, z, 'orange')

plt.show() #sirve para ver todas las figuras creadas en la sesion
