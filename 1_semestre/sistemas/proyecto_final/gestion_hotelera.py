import pandas as pd
import random

# Este programa de gestion se divide en 3 partes;
  # 1. Creacion de variable, simulando una base de datos.
  # 2. Creacion de funciones.
  # 3. Activacion del programa, integrando variables y funciones.

### 1. Asignacion de variables.

opciones_cuartos = {
  'cuarto_1': {
    'coste': 900,
    'capacidad': 3,
    'descripcion': 'Es un cuarto para 3 personas'
  },
  'cuarto_2': {
    'coste': 1250,
    'capacidad': 4,
    'descripcion': 'Es un cuarto '
  },
  'cuarto_3': {
    'coste': 1800,
    'capacidad': 5,
    'descripcion': 'Es un cuarto '
  },
  'cuarto_4': {
    'coste': 2500,
    'capacidad': 3,
    'descripcion': 'Es un cuarto '
  }
}

servicios_extras = {
  'restaurante': {
    'camarones': 110,
    'tacos': 80,
    'refresco': 40
  },
  'lavanderia': {
    'prenda': 20
  }
}

usuario = {
  'nombre': None,
  'direccion': 0,
  'reservacion_guardada': [],
  'servicios_extras': {
    'restaurante': [],
    'lavanderia': []
  },
  'fecha_entrada': '',
  'fecha_salida': ''
}



### 2. Creacion de funciones.
funciones_disponibles = pd.Series(['ver cuartos', 'agregar cuartos', 'calculo de reservacion', 'calculo total', 'agregar servicio', 'factura de restaurante', 'factura de lavanderia', 'help', 'salir'])

def help():
  """
    Es una funcion para mostrar las claves de las funciones
  """
  print('----------------')
  print(f'Las funciones disponibles son:\n{funciones_disponibles}')
  print('----------------\n')


def pedir_datos():
  usuario['nombre'] = input('Ingrese su nombre: ')
  usuario['direccion'] = input('Ingrese su direccion: ')
  usuario['fecha_entrada'] = input('Cuando sera su fecha de entrada?: ')
  usuario['fecha_salida'] = input('Cuando sera su fecha de salida?: ')


def cuartos_fun():
  """
    Es una funcion para manejar la gestion relacionada con los cuartos
  """
  pd_cuartos = pd.DataFrame(opciones_cuartos)

  print(pd_cuartos)
  interesado = input('Interesado en algun cuarto? (Y/n): ')
  if interesado == 'Y':
    opciones = []
    for opcion in opciones_cuartos.keys():
      opciones.append(opcion)

    seleccion = input(f'\nQue cuarto te interesa? las opciones son: \n{opciones}\n')
    if seleccion in opciones:
      cuarto_completo = dict(opciones_cuartos[seleccion])
      # use dict para opciones_cuartos[seleccion] no modificar opciones_cuartos original

      dias = int(input('Cuantas noches se quedara?: '))
      cuarto_completo["dias"] = dias
      print(f"\ntu seleccion fue {seleccion}:\n {cuarto_completo}")
      print(f" - - -Por {dias} noches el precio sera de {dias * cuarto_completo['coste']}")
      r = input('Reservar cuarto? (Y/n): ')
      if r == 'Y':

        q = int(input('Para cuantas personas son?: '))
        if q <= cuarto_completo["capacidad"]:
          cuarto_completo["habitacion"] = random.randint(100, 200)
          usuario["reservacion_guardada"].append(cuarto_completo)
          print('\nRESERVACION COMPLETADA CON EXITO\n')
        else:
          print('El numero de hospedados excede el limite de capacidad. \n')

    else:
      r = ''
      while r != 'reiniciar':
        if r == 'salir': break
        
        r =input('Deseas reiniciar la operacion o salir? (reiniciar/salir):\n')
        if r == 'reiniciar':
          print("\n")
          cuartos_fun()


def cuarto_calculo():
  precio = 0
  for cuarto_completo in usuario['reservacion_guardada']:
    cuarto = pd.Series(cuarto_completo)
    print(f"{cuarto}")
    precio += cuarto_completo["coste"] * cuarto_completo["dias"]
    print('\n')

  return precio


def buscar_alimento():
  """
    Funcion que pide un alimento y lo busca en el menu, para agregarlo a la cuenta del usuario
  """
  r = input('Que alimento te interesa?: ')
  print()
  for item in servicios_extras['restaurante'].items():
    if item[0] == r:
      print(f'Agregaste {item[0]} por {item[1]}\n')
      usuario['servicios_extras']['restaurante'].append(item)


def alimento_calculo():
  final_price = 0
  for price in usuario['servicios_extras']['restaurante']:
    final_price += price[1]
  print('La factura del restaurante contiene:\n')
  print({usuario['servicios_extras']['restaurante']})
  return final_price


def lavanderia_calculo():
  total = 0
  for n in usuario['servicios_extras']['lavanderia']:
    total += n
  print('La factura de la lavanderia contiene:\n')
  print(usuario['servicios_extras']['lavanderia'])
  return total


def servicios_fun():
  servicio = input('Los servicios disponibles son los de "restaurante" y "lavanderia", selecciona alguna de esas 2 opciones: \n')
  
  if servicio == 'restaurante':
    print('Nuestro menu es:\n')
    for item in servicios_extras['restaurante'].items():
      print(f"-- {item[0]} | {item[1]}")
    r = input('Quieres comprar algun producto? (Y/n): ')
    if r == "Y":
      buscar_alimento()
    
  elif servicio == 'lavanderia':
    print(f'El servicio de lavanderia tiene un coste de {servicios_extras["lavanderia"]["prenda"]}')
    r = input('Va a usar el servicio> (Y/n): ')
    if r == 'Y':
      n = int(input('Cuanta prendas va a lavar? '))
      usuario['servicios_extras']['lavanderia'] += [servicios_extras["lavanderia"]["prenda"]] * n
      print(f'Se agrego ${[servicios_extras["lavanderia"]["prenda"]] * n} a tu cuenta \n')
  else:
    print('Ese no es un servicio valido')


def usuario_calculo():
  precio = 0
  precio += cuarto_calculo()
  precio += alimento_calculo()
  precio += lavanderia_calculo()
  print(f"El coste de tus servicios sera de: {precio}")
  
  


def generar_accion(stri):
  """
    Es una funcion guia para cargar una funcion en base a un string
  """
  if 'cuartos' in stri:
    cuartos_fun()
  elif stri == 'calculo total':
    usuario_calculo()
  elif stri == 'agregar servicio':
    servicios_fun()
  elif stri == 'factura de restaurante':
    print(f"La factura del restaurante es de: {alimento_calculo()}")
  elif stri == 'factura de lavanderia':
    print(f"La factura de la lavanderia es de: {lavanderia_calculo()}")
  elif stri == 'calculo de reservacion':
    print(f"El calculo de los cuartos es: {cuarto_calculo()}")
  elif stri == 'help':
    help()


### 3. Activacion del programa.


servicio_activo = True
pedir_datos()
help()

while servicio_activo == True:
  accion = input('\n=========\nIngresa la accion que deseas ejecutar, si necesitas ver las acciones disponibles ingresa help\n=========\n')

  while accion not in funciones_disponibles.values:
    print('=========\nEsa no es una accion valida...')
    accion = input('Que accion deseas hacer, si necesitas ver las acciones disponibles ingresa help\n=========\n')

  print('\n')
  if accion == 'salir':
    servicio_activo = False
    print('\n\n\nMostrando log del hospedaje del usuario:')
    usuario_calculo()
    break

  generar_accion(accion)


