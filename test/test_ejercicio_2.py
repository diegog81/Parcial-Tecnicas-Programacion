import ejercicio_2
import unittest

class Ejercicio2Test(unittest.TestCase):

    def testUnMapaVacioDeberiaDevolverUnaListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = []

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])


    def testUnMapaConEspaciosEnBlancoDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["      "]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaInvalidoDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["soy NO valido"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testOtroMapaInvalidoDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["yo","tambien","soy","invalido"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaConCadenaDeDistintosLongitudesDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b.","....","..bb","b.b"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaValidoDeberiaDevolverPosicionesDeBarcosNoHundidos(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b..","b...b",".....","....b"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [(2,1),(2,5)])


    def testUnMapaSinPosicionesDeDisparosDeberiaDevolverPosicionesDeBarcos(self):

        posicionesDeDisparosDePrueba = []
        mapa = ["b..", "...", "..b"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [(1,1), (3,3)])
