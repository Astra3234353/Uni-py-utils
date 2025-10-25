import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definición de Parámetros y Función de Lennard-Jones ---

# Parámetros de los sistemas
data = {
    'sistema': ['LiF', 'CO', 'Ag2', 'MgO2', 'H2', 'Cu2', 'H2O-H2O'],
    're': [1.5, 1.0, 2.5, 1.75, 0.75, 1.75, 2.25],
    'epsilon': [106.827273, 112.602347, 10352.63362, 272.783896, 1.170601, 3264.8665, 151.954024],
    'sigma': [1.336, 0.890898, 2.2272, 1.559, 0.6682, 1.559, 2.0045]
}
df = pd.DataFrame(data)

def normalized_lennard_jones(r_star):
    r_star = np.where(r_star > 1e-6, r_star, 1e-6) 
    return 4 * ((1.0 / r_star**12) - (1.0 / r_star**6))

r_star_min = 0.8
r_star_max = 3.5
r_star = np.linspace(r_star_min, r_star_max, 500)
V_star = normalized_lennard_jones(r_star)

# Puntos clave para marcar
min_r_star = 2**(1/6)

# --- 2. Iteración para generar un gráfico por cada compuesto ---

print("Generando 7 gráficos individuales...")

for index, row in df.iterrows():
    sistema_nombre = row['sistema']
    
    # 🚨 Crea una figura nueva para cada iteración
    plt.figure(figsize=(10, 6))

    # Plotea la curva universal
    plt.plot(r_star, V_star, label=sistema_nombre, linewidth=3, color='blue')

    # Marcar puntos clave de la curva universal
    plt.plot(min_r_star, -1.0, 'ro', label=r'Mínimo ($\mathbf{V/\epsilon = -1}$)')
    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(1.0, color='green', linestyle=':', label=r'Cruce Cero ($\mathbf{r/\sigma = 1}$)')
    plt.axvline(min_r_star, color='red', linestyle=':', label=r'Equilibrio ($\mathbf{r/\sigma \approx 1.122}$)')

    plt.ylim(-1.2, 2)
    plt.xlim(0.8, 2.5)

    plt.xlabel(r'Distancia Normalizada ($\mathbf{r/\sigma}$)', fontsize=14)
    plt.ylabel(r'Energía Potencial Normalizada ($\mathbf{V(r)/\epsilon}$)', fontsize=14)
    plt.title(f'Potencial de Lennard-Jones Universal para: {sistema_nombre}', fontsize=16)
    plt.legend()
    plt.grid(True, linestyle='--')

    # 🚨 Comando para guardar el gráfico con un nombre único 🚨
    filename = f'LJ_Universal_{sistema_nombre}.png'
    plt.savefig(filename, dpi=300) 
    plt.close() # Cierra la figura en memoria para liberar recursos
    
    print(f"Gráfico guardado: {filename}")

print("\n¡Proceso completado! Se han generado 7 archivos de imagen.")