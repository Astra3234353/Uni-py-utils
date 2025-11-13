# es igual solo que agrega el with

def escribir_tabla(lista):
    with open('archivos.txt','a') as f:
        for elemento in lista:
            f.write('\t'.join(elemento)+'\n') #join une los elementos de una lista con el caracter que le digamos


arreglo=[["Nombre","Edad","Telefono"],["Ana","23","123456"],["Luis","34","654321"],["Pedro","45","987654"]]
escribir_tabla(arreglo)

