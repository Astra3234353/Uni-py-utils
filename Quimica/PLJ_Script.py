import numpy as np

distancia = np.array([
0.5,
1.0,
2.5,
2.0,
3.0,
4.0,
5.0,
7.0
])

energia = np.array([
21.5353395,
1.9525193,
-0.2005134,
-0.2302174,
-0.2094082,
-0.1614058,
-0.1325984,
-0.1092148,
])

def lennard_jones(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

idx_min = np.argmin(energia)
r0 = distancia[idx_min]
Emin = energia[idx_min] # Valor más negativo de la energía de interacción
sigma = r0 / (2**(1/6)) 

epsilon = np.abs(Emin)

# === Mostrar resultados de los parámetros ===
print("=== Parámetros del Potencial de Lennard-Jones ===")
print(f"Distancia de equilibrio (r₀): {r0:.3f} Å")
print(f"Energía mínima (Eₘᵢₙ): {Emin:.6f} Ha")
print(f"Parámetro σ (sigma): {sigma:.4f} Å")
print(f"Parámetro ε (epsilon): {epsilon:.6f} Ha")
print("-------------------------------------------------")
print(f"ε se define como -Eₘᵢₙ: -({Emin:.6f}) = {epsilon:.6f} Ha")

# === Ejemplo: calcular energía teórica LJ en las distancias definidas ===
print("\n=== Energía de Interacción: LJ (Teórico) vs. Gaussian (Dato) ===")
print("r (Å)   |   V_LJ (Ha)    |   E_Gaussian (Ha)")
print("-------------------------------------------------")


for i, r in enumerate(distancia):
    V_lj = lennard_jones(r, epsilon, sigma)
    E_gauss = energia[i]
    print(f"{r:6.2f}   |   {V_lj: .6f}   |   {E_gauss: .6f}")