
def mapaDeDisparos(life,disparo):
    lista = []
    for f in range(len(life)):
        fila = []
        for c in range(len(life[0])):
            fila.append(crearFilaColumna(life,f,c,disparo))
        lista.append(fila)
    return lista

def crearFilaColumna(life,f,c,disparo):

    for x in range(len(disparo)):

        fila = (disparo[x][0])-1
        columna = (disparo[x][1])-1
        if f == fila and c == columna:
            return '.'
    return life[f][c]


def botesNoHundidos(mapa, posicionesDeDisparosDePrueba):
    lista1 = []
    for x in range(1, len(mapa)):
        if len(mapa[x - 1]) != len(mapa[x]):
            return lista1
    lista = mapaDeDisparos(mapa,posicionesDeDisparosDePrueba)
    lista2 = []
    for f in range(len(lista)):
        lista3 = ()
        for c in range(len(lista[0])):
            if lista[f][c] == 'b':
                lista3 = (f+1,c+1)
            if lista != [] and len(lista3) == 2:
                lista2.append(lista3)
                lista3 = []
    return lista2

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]
