# conjuntos 
# son colleciones desprdenadas no indexadas de objetos 
# son inmutables (no se pueden cambiar sus elementos)


x={22, True, "una lista", 3.14, 3j}
y={3.14, "otra lista", False, 7}
x.add("nuevo elemento") #add agrega un elemento
x.remove(3.14)   #remove quita un elemento

if("una lista" in x): #in sirve apra verificar si un elemento esta
    print("si esta")
    
#union juntara los elementos de ambos conjuntos
z=x|y

#interseccion devolcera los elementos que coexisten en ambos conjutos
z=x&y

#diferencia simetrica devoclera que solo estan en un ocnjunto
z=x^y

#DICCIONARIOS

resetario={'nombre':'lalo',
           'edad':22,
           'cursos':['python','java','c++']}

#items devuelve todas la s claves y sus valores
cv=resetario.items()
#keys devuelve todas las claves
k=resetario.keys()
#values devuelve todos los valores
v=resetario.values()
#update cpbina dos diccionarios
resetario.update({'nombre':'juan','telefono':123456789})


#letura y escritura de un archivo de texto

archivo=open('archivo.txt','w') #w es para escribir, r es para leer, a es para agregar
archivo.write('hola mundo\n')
# si el archivo no existe lo crea "w"
# si el archivo no existe marca errar "r"


#taambien exite a es para esribir al final
#b binario
# + lectura y escritura

archivo.read(522) #lee 522 cracteres
archivo.readline() #lee una linea
archivo.readlines() #lee todas las lineas y las devuelve en una lista