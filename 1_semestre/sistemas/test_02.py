lista1 = [1,2]
lista2 = [3,4]

lista3 = lista1 + lista2  # [1, 2, 3, 4]
# print(lista3)

lista1 = [1,10]  # [1, 2, 3, 4]
# print(lista3)

#Cuando sumas listas, no se crea referencia, se crean nuevos datos

final = [None]
a = [1,2]
b= [3,4]

c= a + b
final[0] = c
print(final)