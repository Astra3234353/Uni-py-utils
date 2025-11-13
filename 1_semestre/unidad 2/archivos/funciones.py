def function_inani():
    '''esto es una cadena de documentacion'''
    
    return "Hola, mundo!"


# devolvera la cadena de documentacion
help(function_inani)

# retornar varios vloress 
def area_perim_circle (radio):
    import math
    '''funcion que calcula el area y perimetro de un circulo dado su radio'''
    perim = 2 * math.pi * radio
    area = math.pi * radio**2
    return area, perim


respuestas = area_perim_circle(5)
print(respuestas)

#parametros con valores por defecto
def potencia(base, exponente=2):
    '''funcion que calcula la potencia de un numero'''
    return base ** exponente

#cambiar orden

n_potenciado = potencia(exponente=3, base=2)
print(n_potenciado)

# funciones con parametros infinitos
def suma(*numeros):
    '''funcion que suma una cantidad indeterminada de numeros'''
    total = 0
    for num in numeros:
        total += num
    return total

suma(1,2,3,4,5)
suma(primero=1, segundo=2, tercero=3)

# ahoraa usando diccionaro
def imprimir(**elementos):
    '''funcion que suma una cantidad indeterminada de numeros'''
    for elemento in elementos.items:
        print(elemento)
        
imprimir(x='hola',y='roma')


# asignar funciones a variables

def c_a_f(grados_C):
    '''funcion que convierte grados Celsius a Fahrenheit'''
    return (grados_C * 9/5) + 32

# guardando la funcion en un diccionario
t={'C_a_F': c_a_f}
# usando la funcion a traves del diccionario
t['C_a_F'](30)


def test(**dict):
  for element in dict.items:
    print (element)

test(x="1", y="2")