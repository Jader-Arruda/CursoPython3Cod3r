def recursividade(maximo, atual):
    if atual >= maximo:
        return
    print(atual)
    recursividade(maximo, atual + 1)

recursividade(5,1)