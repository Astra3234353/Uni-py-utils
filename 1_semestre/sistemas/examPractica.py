estEsperados = 5

califTot = []
lista = [None] * 3
calif= [0] * 3
estudiantes = [None] * estEsperados

estNum = 0

for i in range(estEsperados):
  estudiantes[i] = input("\nCual es tu nombre?\n")
  for y in range(3):
    n = int(input('Ingresa tu calificacion del examen %d\n' % (y + 1)))
    lista[y] = n
    calif[y] += n

  califTot += lista
  estNum +=1

print('\n')

# Calculo de calificacion amayor y menor
califMayor = 0
califMenor = 100


b_contador = 1
b_index = 0

for n in califTot:
  if b_contador == 4:
    b_contador = 1
    b_index += 1

  if max(califTot) == n:
    califMayor = n
    print(estudiantes[b_index],'; Tuvo el mayor puntaje de:', max(califTot))

  elif min(califTot) == n:
    califMenor = n
    print(estudiantes[b_index],'; Tuvo el menor puntaje de:', min(califTot))
  
  b_contador += 1

# Mostrar quien tuvo puntos maximos de calificaciones

print('\n')
print('calificaciones:', califTot)
print(estudiantes)
print("Calif final de examen 1 fue: %d" % (calif[0] / estEsperados))
print("Calif final de examen 2 fue: %d" % (calif[1] / estEsperados))
print("Calif final de examen 3 fue: %d\n" % (calif[2] / estEsperados))
print("calif Menor: %d" % califMenor)
print("calif Mayor: %d" % califMayor)
print(estudiantes)


