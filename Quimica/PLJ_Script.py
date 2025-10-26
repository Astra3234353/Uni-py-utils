import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# === Datos experimentales o del cálculo ===
compuesto = 'NaCl'

distancia = np.array([
1,
2.5,
2,
3,
4,
5,
7,
])

energia = np.array([
1.9525193,
-0.2005134,
-0.2302174,
-0.2094082,
-0.1614058,
-0.1325984,
-0.1092148,
])


# 1. Parámetros de Lennard-Jones (LJ)
idx_min = np.argmin(energia)
r0 = distancia[idx_min]
Emin = energia[idx_min]

epsilon = np.abs(Emin)
sigma = r0 / (2**(1/6))

# 2. Función de potencial de Lennard-Jones (LJ)
def lennard_jones(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# 3. Generar la curva teórica de LJ
r_curve_lj = np.linspace(0.5, 7.0, 300) 
V_lj_curve = lennard_jones(r_curve_lj, epsilon, sigma)

# 4. Interpolación para curva suave de datos Gaussian
sorted_indices = np.argsort(distancia)
interp_func = interp1d(distancia[sorted_indices], energia[sorted_indices], kind='cubic')
r_interp = np.linspace(np.min(distancia), np.max(distancia), 300)
E_interp = interp_func(r_interp)


# 5. CONFIGURACIÓN DINÁMICA ÓPTIMA DE LÍMITES
# La nueva energía máxima es -0.98, la multiplicación por 1.25 daría un valor más negativo (incorrecto).
# Usamos el 0.0 como referencia superior.
E_max_foco = np.max(energia) 
E_min_total = np.min(energia)

y_lim_min = E_min_total - 0.25  # Margen de 0.25 para el mínimo
y_lim_max = 2   # Margen de 0.25 para el máximo (cercano a 0)

x_lim_min = np.min(distancia) - 0.1
x_lim_max = np.max(distancia) + 0.5 

# 6. Generar la gráfica
plt.figure(figsize=(10, 6))

# Graficar los puntos de Gaussian y la línea curva suave
plt.plot(distancia, energia, 
         marker='o', linestyle='None', color='red', markersize=6)
plt.plot(r_interp, E_interp, 
         linestyle='-', color='red', linewidth=1.5,
         label='Valores de Gaussian')

# Graficar la curva ajustada de Lennard-Jones
plt.plot(r_curve_lj, V_lj_curve, 
         linestyle='-', color='blue', linewidth=2, 
         label=f'Lennard-Jones Ajustado')

# Línea horizontal para marcar E=0
plt.axhline(0, color='black', linestyle='-', linewidth=1.0) 

# Líneas verticales para marcar puntos clave
plt.axvline(r0, color='green', linestyle=':', linewidth=1.5, 
            label=r'$r_0$ (Mínimo LJ) = ' + f'{r0:.2f} $\mathrm{{\AA}}$')
plt.plot(r0, Emin, marker='s', color='green', markersize=8)

plt.axvline(sigma, color='purple', linestyle=':', linewidth=1.5, 
            label=r'$\sigma$ (Cero LJ) = ' + f'{sigma:.2f} $\mathrm{{\AA}}$')


# Configuración de la gráfica
plt.title(f'Potencial de Lennard-Jones vs. Energía de Interacción del {compuesto}')
plt.xlabel(r'Distancia Interatómica ($r$, $\mathrm{\AA}$)')
plt.ylabel(r'Energía ($\mathrm{Ha}$)')

# Aplicar límites DINÁMICOS OPTIMIZADOS
plt.ylim(y_lim_min, y_lim_max)
plt.xlim(x_lim_min, x_lim_max)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# 7. Guardar la gráfica como PNG
png_filename = f'LJ_Universal_{compuesto}.png'
plt.savefig(png_filename)


# =======================================================
# 8. LOG DEL POTENCIAL EN CONSOLA
# =======================================================

print("\n" + "="*70)
print(f"--- LOG DE ENERGÍA DE INTERACCIÓN ({compuesto}) ---")
print(f"Parámetros LJ: epsilon={epsilon:.6f}, Ha ={sigma:.6f} Å")
print("="*70)
print(f"{'Distancia (Å)':<15} | {'E_Gaussian (Ha)':<20} | {'U_LennardJones (Ha)':<20} | {'Error Absoluto':<15}")
print("-" * 70)

for r_val, E_gauss in zip(distancia, energia):
    # Calcular el valor teórico de LJ
    U_lj = lennard_jones(r_val, epsilon, sigma)
    # Calcular el error absoluto
    error = np.abs(E_gauss - U_lj)
    
    print(f"{r_val:<15.2f} | {E_gauss:<20.6f} | {U_lj:<20.6f} | {error:<15.6f}")

print("-" * 70)
print(f"Gráfica guardada como: {png_filename}")
print("="*70 + "\n")