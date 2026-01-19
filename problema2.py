import string

def frecuencia_palabras(lista_palabras, ruta_fichero):
    #Inicializar diccionario con frecuencia 0
    frecuencias = {palabra.lower(): 0 for palabra in lista_palabras}

    #Leemos el texto (pasandolo a minusculas)
    with open(ruta_fichero, "r", encoding="utf-8") as f:
        texto = f.read().lower()

    #Quitamos signos puntuacion
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    #Separamos el texto en palabras
    palabras_texto = texto.split()

    #Vemos frecuencias
    for palabra in palabras_texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

    return frecuencias


if __name__ == "__main__": #Por si se importa para pruebas automatizadas
    lista = ["lorem", "sit", "ex", "et"]
    ruta = "texto.txt"

   
    print(frecuencia_palabras(lista, ruta))
   
   