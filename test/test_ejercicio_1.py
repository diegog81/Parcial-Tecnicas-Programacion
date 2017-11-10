import ejercicio_1
import unittest

class EjercicioTest(unittest.TestCase):
    def testRotacionesSiNoRecibeNadaDeberiaDevolverListaVacia(self):
        #arrange
        palabra = ""

        #act
        resultado = ejercicio_1.rotaciones(palabra)

        #assert
        self.assertEqual(resultado,[])

    def testRotacionesSiRecibeUnoOMasEspaciosDeberiaDevolverListaVacia(self):

        palabra = "     "

        resultado = ejercicio_1.rotaciones(palabra)

        self.assertEqual(resultado,[])

    def testRotacionesSiRecibeUnaLetraDeberiaDevolverLaMismaLetra(self):

        palabra = "a"

        resultado = ejercicio_1.rotaciones(palabra)

        self.assertEqual(resultado,['a'])

    def testRotacionesSiRecibeUnaPalabraDeberiaDevolverPalabraEnOrdenInverso(self):

        palabra = "ab"

        resultado = ejercicio_1.rotaciones(palabra)

        self.assertEqual(resultado,['ab','ba'])

    def testRotacionesSiRecibeUnaPalabraPazDeberiaDevolverPalabraEnOrdenInverso(self):

        palabra = "paz"

        resultado = ejercicio_1.rotaciones(palabra)

        self.assertEqual(resultado,['paz','azp','zpa'])

    def testRotacionesSiRecibeUnaPalabraSolDeberiaDevolverPalabraEnOrdenInverso(self):

        palabra = "so l"

        resultado = ejercicio_1.rotaciones(palabra)

        self.assertEqual(resultado,['so l','o ls',' lso','lso '])

    def testRotacionesSiRecibeUnaPalabraRotarDeberiaDevolverPalabraEnOrdenInverso(self):

        palabra = "rotar"

        resultado = ejercicio_1.rotaciones(palabra)

        self.assertEqual(resultado,['rotar','otarr','tarro','arrot','rrota'])