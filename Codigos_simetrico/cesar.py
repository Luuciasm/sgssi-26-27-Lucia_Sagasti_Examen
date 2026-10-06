#python
from langdetect import detect
#langdetect sirve para detectar el idioma de un texto.

mensaje = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

alfabeto = "abcdefghijklmnopqrstuvwxyz"

for clave in range(26):
    #probamos todas las claves posibles (0-25) para descifrar el mensaje.

    texto = "" # Variable para almacenar el texto descifrado.

    for letra in mensaje:

        if letra.lower() in alfabeto: # Si la letra está en el alfabeto en minusculas.
            posicion = alfabeto.index(letra.lower()) #nos dice la posición de la letra en el alfabeto.
            nueva_posicion = (posicion - clave) % 26 # Calcula la nueva posición de la letra en el alfabeto, desplazamiento hacia atras, el %26 es para volver a empezar si se pasa del final.
            nueva_letra = alfabeto[nueva_posicion] # Obtiene la nueva letra del alfabeto.

            if letra.isupper(): # Si la letra original es mayúscula, convertimos la nueva letra a mayúscula.
                nueva_letra = nueva_letra.upper() #

            texto = texto + nueva_letra # Añade la nueva letra al texto descifrado.

        else:
            texto = texto + letra # Si la letra no está en el alfabeto, la añadimos tal cual al texto descifrado, espacios o signos de puntuación.

    if detect(texto) == "es": # Si el texto descifrado es en español.
        print("Clave:", clave) # Imprime la clave utilizada para descifrar el mensaje.
        print("Mensaje:", texto) # Imprime el mensaje descifrado.
