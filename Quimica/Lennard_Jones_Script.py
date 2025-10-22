import numpy as np

# === Datos experimentales o del cálculo (NaCl) ===
distancia = np.array([1, 1.15, 1.3, 1.45, 1.6, 1.75, 1.9, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])

energia = np.array([
    -617.1530787, -618.0387613, -618.5746971, -618.9167651, -619.1279536,
    -619.2522298, -619.3225508, -619.3506835, -619.3917382, -619.3829489,
    -619.368872, -619.357118, -619.3487866, -619.3431893, -619.3393393, -619.336579
])




# === Ecuación del potencial de Lennard-Jones ===
# V(r) = 4ε * [ (σ/r)^12 - (σ/r)^6 ]

def lennard_jones(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)

# === Estimación aproximada de parámetros ===
# Tomamos r0 donde E es mínima → distancia de equilibrio
idx_min = np.argmin(energia)
r0 = distancia[idx_min]
Emin = energia[idx_min]

# Para el potencial de Lennard-Jones, se cumple:
# r0 = 2^(1/6) * σ  →  σ = r0 / 2^(1/6)
sigma = r0 / (2 ** (1/6))

# ε es la profundidad del pozo de potencial (valor absoluto de E mínima)
# Aquí solo tomamos la diferencia respecto al valor más alto como referencia
epsilon = abs(Emin - energia[-1])





# === Mostrar resultados ===
print("=== Potencial de Lennard-Jones ===")
print(f"Distancia de equilibrio (r₀): {r0:.3f} Å")
print(f"Energía mínima (Eₘᵢₙ): {Emin:.6f}")
print(f"Parámetro σ (sigma): {sigma:.4f} Å")
print(f"Parámetro ε (epsilon): {epsilon} (unidades de energía)")
print(Emin, energia[0])



# === Ejemplo: calcular energía teórica LJ en las distancias definidas ===
print("r (Å)   |   V_LJ (energía relativa)")
print("------------------------------------")
for r in distancia:
    V = lennard_jones(r, epsilon, sigma)
    print(f"{r:6.2f}   |   {V: .6f}")
