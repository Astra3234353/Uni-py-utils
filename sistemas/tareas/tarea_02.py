import random

up_lim = int(input('Ingresa el limite superior de tu rango: \n'))
bott_lim = int(input('Ingresa el limite inferior de tu rango: \n'))

secret_num = random.randint(bott_lim, up_lim)
user_num = None

while user_num != secret_num:
  user_num = int(input('Adivina el número secreto: '))

  if user_num < secret_num:
    print('Demasiado bajo...')
  elif user_num > secret_num:
    print('Demasiado alto.10..')
  elif user_num == secret_num:
    print('Ganaste!')