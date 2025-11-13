#open devuelve un objeto FILE qie permite manipular el archivo

NombreArchivo= 'archivos.txt'
f = open(NombreArchivo, 'w')
f.write('Hola Mundo')
f.close() 


# archivo con ruta

# NombreArchivo2 = 'C:\Users\inani\downloads\archivo2.txt'
# fexterno = open(NombreArchivo2, 'w') #r de read
# fexterno.write('Hola Mundo')
# fexterno.close()

f = open(NombreArchivo, 'a')
f.seek(10)
f.write('\nHola Mundo 2')
f.close() 

#imprimir lista en archivo
lista = ['Linea 1', 'Linea 2', 'Linea 3']
f = open(NombreArchivo, 'a')

for linea in lista:
    f.write( linea + '\n')
f.close()

#imprimir tabla en archivo
f = open(NombreArchivo, 'a')

for i in range(0,3):
    for elemento in lista:
        f.write(elemento + '\t')
    f.write('\n')
f.close()    
