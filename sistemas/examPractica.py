estEsperados = 3

califTot = [None] * estEsperados
lista = [None] * 3
calif= [None] * 3

estNum = 0

for i in range(estEsperados):
  for y in range(3):
    n = int(input('Ingresa tu calid del examen %d\n' % y))
    lista[y] = n
    calif[y] += n

  califTot[i] = lista

  estNum +=1

