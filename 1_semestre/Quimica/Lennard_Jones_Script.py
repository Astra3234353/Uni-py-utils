import numpy as np

# === Datos experimentales o del cálculo (NaCl) ===
distancia = np.array([
0.5,
1,
2.5,
2,
3,
4,
5,
7
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
Emin = energia[idx_min]


print(lennard_jones(4.0, 0.997, 3.40))