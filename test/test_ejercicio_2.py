import ejercicio_2
import unittest

class EjercicioTest(unittest.TestCase):

    def testUnMapaVacioDeberiaDevolverUnaListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = []

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado,[])


    def testUnMapaVacioDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = []

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaConEspaciosEnBlancoDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["      "]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaConUnStringDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["soy NO valido"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaConUnaCadenaDeCaracteresDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["yo","tambien","soy","invalido"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaConCadenaDeDistintosLenDeberiaDevolverListaVacia(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b.","....","..bb","b.b"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [])


    def testUnMapaConListaDeCadenasDeberiaDevolverPosicionesDeBarcosNoHundidos(self):

        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        mapa = ["b.b..","b...b",".....","....b"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [(2,1),(2,5)])


    def testUnMapaSinPosicionesDeDisparosDeberiaDevolverPosicionesDeBarcos(self):

        posicionesDeDisparosDePrueba = []
        mapa = ["b..", "...", "..b"]

        resultado = ejercicio_2.botesNoHundidos(mapa, posicionesDeDisparosDePrueba)

        self.assertEqual(resultado, [(1,1), (3,3)])
