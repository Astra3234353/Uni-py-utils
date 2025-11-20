import pandas as pd

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
    'menu': ('Camarones', 'Orden de tacos', 'Refresco'),
    'menu_precios': (110, 85, 40)
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
funciones_disponibles = pd.Series(['ver cuartos', 'agregar cuartos', 'precio total', 'agregar servicio', 'calculo cuarto', 'help', 'salir'])

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
  # Recuerda preguntar si se puede usar Dates para calcular y tener fechas de entrada y salida, o uso de catch para manejo de ingreso de datos incorrectos
  usuario['fecha_salida'] = int(input('Cuantas noches va a durar?: '))


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
      print(f"\ntu seleccion fue {seleccion}:\n {opciones_cuartos[seleccion]}")
      print(f" - - -Por {usuario['fecha_salida']} noches el precio sera de {usuario['fecha_salida'] * opciones_cuartos[seleccion]['coste']}")

      r = input('Reservar cuarto? (Y/n): ')
      if r == 'Y':
        q = int(input('Para cuantas personas son?: '))
        if q <= opciones_cuartos[seleccion]["capacidad"]:
          usuario["reservacion_guardada"].append(opciones_cuartos[seleccion])
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


def generar_accion(stri):
  """
    Es una funcion guia para cargar una funcion en base a un string
  """
  if 'cuartos' in stri:
    cuartos_fun()
  elif stri == 'precio total':
    usuario_calculo()
  elif stri == 'agregar servicio':
    print('Viendo cuartos...')
  elif stri == 'calculo cuarto':
    print(cuarto_calculo())
  elif stri == 'help':
    help()


def cuarto_calculo():
  precio = 0
  for cuarto in usuario['reservacion_guardada']:
    precio += cuarto["coste"] * usuario['fecha_salida']

  return precio


def servicio_factura():
  pass


def usuario_calculo():
  precio = 0
  precio += cuarto_calculo()
  # calculo por alimentos...
  print(f"El coste de tus servicios sera de: {precio}")


### 3. Activacion del programa.
servicio_activo = True
pedir_datos()
help()

while servicio_activo == True:
  accion = input('\n=========\nQue accion deseas hacer, si necesitas ver las acciones disponibles ingresa help\n=========\n')

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


