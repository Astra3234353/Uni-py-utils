import pandas as pd
import matplotlib.pyplot as plt

serie = pd.Series({
  'coche': 4,
  'comida': 5,
  'personas': 4
})

dataFrame = pd.DataFrame({
  'nombres': ['alejandro', 'Luis', 'Hector'],
  'edad': [18, 17, 18],
  'correos': ['alex@gmail.com', 'Luisgamer@gmail.com', 'Hectorsito@gmil.com']
})

print(serie)
print(dataFrame)