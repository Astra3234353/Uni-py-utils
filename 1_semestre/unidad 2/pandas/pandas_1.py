import pandas as pd

# Se puede poner una lista o diccionario
# Tienen que ser del mismo tipo
s = pd.Series({'Matematicas': 6.0, 'Sistemas': 5.0, 'Historia': 10})

print(s.size)
print(s.index)
print(s['Matematicas'])


datos = {
    'nombres': ['Alex', 'Luis', 'Jesus'],
    'grado': ['5', '2', '3'],
    'email': ['alejandroleonlpz@gmail.com', 'luisgame@gmail.com', 'jesusTheGod69@yahoo.com']
  }

datos2 = [['Alex', '5'], ['Luis', '2'], ['Jesus', '3']]

dataFrame = pd.DataFrame(datos)
dataFrame2 = pd.DataFrame(datos2, columns=['nombres', 'grado'])


print(dataFrame)
print(dataFrame2)
