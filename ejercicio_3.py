
def ordenaNombres(tupla):
    lista = []
    for x in range(len(tupla)):
        lista.append(tupla[x][0])
    lista1 = []
    for x in sorted(set(lista)):
        lista1.append(x)
    return (lista1[0])


def comparaSiSonIguales(tupla):
    lista = empaquetaTupla(tupla)
    lista = empaquetaLista(lista)
    for x in range(1, len(lista)):
        if lista[x-1][1] == lista[x][1]:
            continue
        else:
            return False
    return True


def empaquetaTupla(tupla):
    lista = []

    for x in range(len(tupla)):
        lista1 = []
        for y in range(1, len(tupla[0]), 2):
            lista1.append(tupla[x][y - 1])
            lista1.append(tupla[x][y])

        lista.append(lista1)
    return lista


def empaquetaLista(lista):
    equipo = []

    for x in range(len(lista)):
        equipo1 = []
        for y in range(0, len(lista[0])):
            equipo1 = []
            if type(lista[x][y]) == int:
                equipo1.append(lista[x][y - 1])
                equipo1.append(lista[x][y])
            if equipo1 != []:
                equipo.append(equipo1)

    return equipo


def ganadorDelCampeonato(tupla):
    if tupla == []:
        return ""
    lista = empaquetaTupla(tupla)
    lista = empaquetaLista(lista)
    if comparaSiSonIguales(lista) == True:
        return ordenaNombres(lista)

    puntaje = 0
    for x in range(len(lista)):

        for i in range(len(lista)):
            if lista[x][1] > lista[i][1]:
                puntaje = lista[x]

    resultado = puntaje[0]
    return resultado
