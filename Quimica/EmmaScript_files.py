import os


VALOR_A_REEMPLAZAR = "1.00000000" 

Z_INICIAL = 2.0
Z_FINAL = 6.0

# --- 1. Pedir datoa al usuario ---

NOMBRE_PLANTILLA = input("Ingrese el nombre del archivo plantilla: ")
NOMBRE_PLANTILLA = f'{NOMBRE_PLANTILLA}.gjf'
nombreArchivoGenerado= input("Ingrese el nombre base para los archivos generados (e.g., LIF, litio-fluor): ")
salto_str = input("De cuanto sera el incremento de la coordenada Z (e.g., 0.25, 0.5)? ")
salto = float(salto_str)

# --- 2. Leer Contenido del Archivo Plantilla ---
with open(NOMBRE_PLANTILLA, 'r', encoding='utf-8') as archivo:
    contenido_plantilla = archivo.read()
print(f"\nPlantilla '{NOMBRE_PLANTILLA}' cargada con éxito.")


# --- 3. Generar Archivos Modificados ---

valor_actual = Z_INICIAL
contador_archivos = 0

while valor_actual <= Z_FINAL+salto/2:
    
    nombre_nuevo_archivo = f"{nombreArchivoGenerado}_{int(valor_actual*100)}.gjf"
    valor_formateado_str = f"{valor_actual:.8f}"
    contenido_modificado = contenido_plantilla.replace(VALOR_A_REEMPLAZAR, valor_formateado_str)

    with open(nombre_nuevo_archivo, "w", encoding='utf-8') as archivo_nuevo:
        archivo_nuevo.write(contenido_modificado)
        
    print(f"Archivo '{nombre_nuevo_archivo}' creado con valor Z: {valor_formateado_str}")

    valor_actual += salto
    contador_archivos += 1
    
print(f"\nProceso de creación de archivos finalizado. Total de archivos creados: {contador_archivos}.")
