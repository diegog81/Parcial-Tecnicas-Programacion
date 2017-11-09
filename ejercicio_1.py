def rotaciones(palabra):
    lista = []
    caracter = 0
    try:
        caracter = palabra.split(" ")
        if caracter[0] == '' and caracter[1] == '':
            return lista
    except:
        caracter = 0
    if type(palabra) == str:
        lista2 = list(palabra)
        lista.append(lista2)
        p = []
        for x in range(len(palabra)):
            p = lista[x]
            lista1 = []
            for i in range(1,len(palabra)):
                lista1.append(p[i])
            lista1.append(p[0])
            lista.append(lista1)
        r = []
        for x in range(len(lista)-1):
            r.append(''.join(lista[x]))
        return r
    else:
        return lista

