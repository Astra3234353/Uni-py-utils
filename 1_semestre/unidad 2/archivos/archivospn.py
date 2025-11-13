 
def escribir_tabla(lista):
    nombre_archivo="archivos.txt"
    f=open('archivos.txt','a')
    for elemento in lista:
        for subelemento in elemento:
            f.write(subelemento+'\t')
        f.write('\n')
    f.close()


arreglo=[["Nombre","Edad","Telefono"],["Ana","23","123456"],["Luis","34","654321"],["Pedro","45","987654"]]
escribir_tabla(arreglo)

