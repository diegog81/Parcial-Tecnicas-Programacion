import ejercicio_3
import unittest

class EjercicioTest(unittest.TestCase):
    def testResultadoDelGanadorSiRecibeUnaListaVaciaDeberiaDevolverVacio(self):

        tupla = []

        resultado = ejercicio_3.resultadoDelGanador(tupla)

        self.assertEqual(resultado, "")


    def testResultadoDelGanadorSiRecibeUnaListaConUnaTuplaDeEquiposDeberiaDevolverEquipoConMayoresGoles(self):

        tupla = [("a", 1, "b", 0)]

        resultado = ejercicio_3.resultadoDelGanador(tupla)

        self.assertEqual(resultado, "a")


    def testResultadoDelGanadorSiRecibeUnaListaConTresTuplasDeEquiposDeberiaDevolverEquipoConMayorPuntaje(self):

        tupla = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        resultado = ejercicio_3.resultadoDelGanador(tupla)

        self.assertEqual(resultado, "c")


    def testResultadoDelGanadorSiRecibeUnaListaConTresTuplasDeEquiposConPuntosEmpatadosDeberiaDevolverElPrimeroEnOrdenAlfabetico(self):

        tupla = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        resultado = ejercicio_3.resultadoDelGanador(tupla)

        self.assertEqual(resultado, "Almagro")


    def testResultadoDelGanadorSiRecibeUnaListaConCuatroTuplasDeEquiposDeberiaDevolverEquipoConMayorPuntaje(self):

        tupla = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        resultado = ejercicio_3.resultadoDelGanador(tupla)

        self.assertEqual(resultado, "a")
