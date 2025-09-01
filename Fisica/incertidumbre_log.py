import math

# Datos
values = [
2.517,
4.089,
3.562,
3.604,
3.958,
4.155,
3.72,
3.019,
2.513,
3.759,
3.516,
3.806,
3.767,
3.459,
4.38,
3.425,
3.606,
2.44,
3.821,
3.418,
]
div_escala = 0.01

# Paso 1 
media = sum(values) / len(values)

Ud = div_escala / (2 * math.sqrt(3))

# Paso 2 
suma_cuadrados = 0
for value in values:
    suma_cuadrados += (value - media) ** 2


# Paso 3
desv_std = math.sqrt(suma_cuadrados / (len(values) * (len(values) - 1)))
U = math.sqrt((desv_std)**2 + (Ud)**2 )

print(f"\n\033[32mDatos:... \033[0m")
print(f"Media = {media}")
print(f"Desviación estándar (muestral) = {desv_std}")
print(f"Ud: {Ud}")
print(f'U: {U}')
print('\n')

print(f"N: {len(values)}")
print(f"({media} +- {U})")

