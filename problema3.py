def analisis_conjuntos(lista1, lista2):
    
    conjunto1 = set(lista1)
    conjunto2= set(lista2)

    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia = conjunto1 ^ conjunto2

    diccionario ={
        "Interseccion" : interseccion,
        "Union": union,
        "Diferencia_simetrica": diferencia
    }

    return diccionario

if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]

    print(analisis_conjuntos(lista1, lista2))