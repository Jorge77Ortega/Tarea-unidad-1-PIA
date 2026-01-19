def limpiar_lista(lista):
    # Quitamos los numeros negativos
    lista_sin_negativos = [i for i in lista if i>=0]
    # Quitamos los numeros repetidos
    lista_sin_repetidos = list(set(lista_sin_negativos))
    # Ordenamos la lista
    lista_ordenada = sorted(lista_sin_repetidos)

    return lista_ordenada

prueba = [4,-1,2,4,3,-5,2]
print(limpiar_lista(prueba))
