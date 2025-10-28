import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

compuesto = input('Cual es el compuesto?')

distancia = np.array([
0.9,
1.5,
1.7,
1.9,
2.1,
2.7,
3.3,
3.9,
4.5,
5.1,
5.7
])

energia_no_ajustada = np.array([
5.664158,
0.572618,
0.316278,
0.208739,
0.170185,
0.195363,
0.244035,
0.244035,
0.28374,
0.289328,
0.291893
])





# Calculos

#!!!!!!!!!!! Ajuste de energias
energia = np.array([x - energia_no_ajustada[-1] for x in energia_no_ajustada])

idx_min = np.argmin(energia)
r0 = distancia[idx_min]
Emin = energia[idx_min]

epsilon = np.abs(Emin)
sigma = r0 / (2**(1/6))

# Función de potencial de Lennard-Jones
def lennard_jones(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# Curva
r_curve_lj = np.linspace(0.5, 7.0, 300) 
V_lj_curve = lennard_jones(r_curve_lj, epsilon, sigma)

sorted_indices = np.argsort(distancia)
interp_func = interp1d(distancia[sorted_indices], energia[sorted_indices], kind='cubic')
r_interp = np.linspace(np.min(distancia), np.max(distancia), 300)
E_interp = interp_func(r_interp)




E_max_foco = np.max(energia) 
E_min_total = np.min(energia)

y_lim_min = E_min_total - 0.25 
y_lim_max = 2   

x_lim_min = np.min(distancia) - 0.1
x_lim_max = np.max(distancia) + 0.5 

# Grafica
plt.figure(figsize=(10, 6))

plt.plot(distancia, energia, 
         marker='o', linestyle='None', color='red', markersize=6)
plt.plot(r_interp, E_interp, 
         linestyle='-', color='red', linewidth=1.5,
         label='Valores de Gaussian')

plt.plot(r_curve_lj, V_lj_curve, 
         linestyle='-', color='blue', linewidth=2, 
         label=f'Lennard-Jones Ajustado')

plt.axhline(0, color='black', linestyle='-', linewidth=1.0) 

plt.axvline(r0, color='green', linestyle=':', linewidth=1.5, 
            label=r'$r_0$ (Mínimo LJ) = ' + f'{r0:.2f} $\mathrm{{\AA}}$')
plt.plot(r0, Emin, marker='s', color='green', markersize=8)

plt.axvline(sigma, color='purple', linestyle=':', linewidth=1.5, 
            label=r'$\sigma$ (Cero LJ) = ' + f'{sigma:.2f} $\mathrm{{\AA}}$')

plt.axvline(label=f'ε = {epsilon:.3f}')


# Configuración de la gráfica
plt.title(f'Potencial de Lennard-Jones vs. Energía de Interacción del {compuesto}')
plt.xlabel(r'Distancia Interatómica ($r$, $\mathrm{\AA}$)')
plt.ylabel(r'Energía ($\mathrm{Ha}$)')

plt.ylim(y_lim_min, y_lim_max)
plt.xlim(x_lim_min, x_lim_max)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

png_filename = f'LJ_Universal_{compuesto}.png'
plt.savefig(png_filename)


# =======================================================
# 8. LOG DEL POTENCIAL EN CONSOLA
# =======================================================

print("\n" + "="*70)
print(f"--- LOG DE ENERGÍA DE INTERACCIÓN ({compuesto}) ---")
print(f"Parámetros LJ: epsilon={epsilon:.6f}, Ha ={sigma:.6f} Å")
print("="*70)
print(f"r0 = {r0}")
print(f"{'Distancia (Å)':<15} | {'E_Gaussian (Ha)':<20} | {'U_LennardJones (Ha)':<20} | {'Error Absoluto':<15}")
print("-" * 70)

for r_val, E_gauss in zip(distancia, energia):
    U_lj = lennard_jones(r_val, epsilon, sigma)
    error = np.abs(E_gauss - U_lj)
    
    print(f"{r_val:<15.2f} | {E_gauss:<20.6f} | {U_lj:<20.6f} | {error:<15.6f}")

print("-" * 70)
print(f"Gráfica guardada como: {png_filename}")
print("="*70 + "\n")