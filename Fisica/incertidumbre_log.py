import math


# Datos (Cambiar)
"""
    En values pon los valores de cada variables. Y en caso de ser necesario, modifica la division de escala.
"""
values = [9.246, 3.416, 3.206, 5.631, 4.165, 5.377, 3.347, 3.423, 3.864, 4.679]
div_escala = 0.001




# Calculos
media = sum(values) / len(values)

Ud = div_escala / (2 * math.sqrt(3))

suma_cuadrados = 0
for value in values:
    suma_cuadrados += (value - media) ** 2

desv_std = math.sqrt(suma_cuadrados / (len(values) * (len(values) - 1)))
U = math.sqrt((desv_std)**2 + (Ud)**2 )


#Log
print(f"\n\033[32mDatos:... \033[0m")
print(f"Media = {media}")
print(f"Desviación estándar (muestral) = {desv_std}")
print(f"Ud: {Ud}")
print(f'U: {U}')
print('\n')

print(f"Numero de valores: {len(values)}")
print(f"\033[32mIncertidumbre:({round(media, 3)} ± {round(U, 3)})\n\033[0m")

