estEsperados = 3

califTot = []
lista = [None] * 3
calif= [0] * 3

estNum = 0

for i in range(estEsperados):
  for y in range(3):
    n = int(input('Ingresa tu calid del examen %d\n' % (y + 1)))
    lista[y] = n
    calif[y] += n

  califTot += lista
  estNum +=1

print(califTot)
print(calif)
print("Calif final de examen 1 fue: %d" % (calif[0] / estEsperados))
print("Calif final de examen 2 fue: %d" % (calif[1] / estEsperados))
print("Calif final de examen 3 fue: %d" % (calif[2] / estEsperados))


