import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-2, 3), 1)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(-5, -3), -2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(-2, -3), 6)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-6, -3), 2)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
