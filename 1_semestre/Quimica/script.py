import numpy as np

distancia = np.array([
1,
1.25,
1.5,
1.75,
2,
2.25,
2.5,
2.75,
3,
3.25,
3.5,
3.75,
4,
4.25,
4.5,
4.75,
5,
5.25,
5.5,
5.75,
6
])

energia_no_ajustada = np.array([
0.774203,
0.04192,
-0.180555,
-0.208228,
-0.200741,
-0.179217,
-0.14973,
-0.119995,
-0.092898,
-0.069433,
-0.049698,
-0.033423,
-0.020459,
-0.011788,
-0.006708,
-0.003796,
-0.002154,
7.5E-05,
8.6E-05,
8.4E-05,
7.2E-05,
])

energia = np.array([x - energia_no_ajustada[-1] for x in energia_no_ajustada])

idx_min = np.argmin(energia)
r0 = distancia[idx_min]
Emin = energia[idx_min]

epsilon = np.abs(Emin)
sigma = r0 / (2**(1/6))

def lennard_jones(r, epsilon, sigma):
    return 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)


print(f"sigma: {sigma}")
print(f'epsilon: {epsilon}')