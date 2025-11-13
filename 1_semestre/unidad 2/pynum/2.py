import numpy as np
import matplotlib.pyplot as plt

u = np.array([3, 4])
v = np.array([1, 2])

# Configuramos los límites del gráfico para que el vector sea visible
max_coord = max(abs(u).max(), abs(v).max()) + 1

# Ploteamos el vector u
plt.figure(figsize=(6, 6))
plt.arrow(0, 0, u[0], u[1], head_width=0.2, head_length=0.3, fc='blue', ec='blue', label='Vector u')

# Configuramos la cuadrícula, los ejes y la relación de aspecto
plt.xlim(0, max_coord)
plt.ylim(0, max_coord)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Visualización del Vector u')
plt.grid(True, linestyle='--', alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()

# Guardamos el plot
plt.savefig('vector_u_plot.png')