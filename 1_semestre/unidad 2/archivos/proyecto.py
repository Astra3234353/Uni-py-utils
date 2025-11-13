import random as rd

linf = int(input("Ingrese el límite inferior: "))
lsup = int(input("Ingrese el límite : "))
numero= int(rd.uniform(linf, lsup))
intentos = 0
n_ingresado= 0

print('ahora adivina el numero....\n')

while n_ingresado != numero:
    n_ingresado = int(input('numero:'))
    if n_ingresado < numero:
        print('el numero es menor')
    elif n_ingresado > numero:
        print('el numero es mayor')
    intentos += 1
print(f'felicidades, lo has logrado en {intentos} intentos')
    