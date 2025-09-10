estEsperados = 5

califTot = 0
estNum = 0

while estEsperados > estNum:
  num = int(input('Cual fue tu calificacion? \n'))
  califTot += num
  estNum +=1

media = califTot / estNum

print('La calificacion total fue de: %d' % califTot)
print('La media es de: %d' % media)
