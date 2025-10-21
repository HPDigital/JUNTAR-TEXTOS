"""
JUNTAR TEXTOS
"""

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

def juntar_txt(directorio, archivo_salida):
    # Abrimos el archivo de salida en modo escritura
    with open(archivo_salida, 'w', encoding='utf-8') as archivo_final:
        # Iteramos sobre todos los archivos .txt en el directorio
        for nombre_archivo in os.listdir(directorio):
            if nombre_archivo.endswith(".txt"):
                ruta_archivo = os.path.join(directorio, nombre_archivo)
                # Abrimos cada archivo .txt y lo añadimos al archivo final
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                    contenido = archivo_txt.read()
                    archivo_final.write(contenido + '\n')  # Añadimos un salto de línea al final de cada archivo

    print(f"Archivos .txt combinados en: {archivo_salida}")

# Ejemplo de uso
directorio = r"C:\Users\HP\Desktop\LIBROS PERSO\INVESTIGACION DE MERCADOS\TEXTOS INVESTIGACION DE MERCADO\TEXTOS"  # Cambia esta ruta por la del directorio que contiene los archivos .txt
archivo_salida = r"C:\Users\HP\Desktop\LIBROS PERSO\INVESTIGACION DE MERCADOS\TEXTOS INVESTIGACION DE MERCADO\TEXTOS\archivo_final.txt"  # Cambia esta ruta por la ubicación donde quieras guardar el archivo final

juntar_txt(directorio, archivo_salida)


# In[ ]:






if __name__ == "__main__":
    pass
