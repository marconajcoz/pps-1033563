import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicacion(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(3, 4), 12)
        self.assertEqual(calc.multiplicar(2, 2), 4)
        self.assertEqual(calc.multiplicar(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
