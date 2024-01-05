import calculadora
import unittest

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.suma(3,5),8)
        self.assertEqual(calculadora.suma(-1,1),0)
        self.assertEqual(calculadora.suma(0,0),0)
    def test_resta(self):
        self.assertEqual(calculadora.resta(4,3),1)
        self.assertEqual(calculadora.resta(0,5),-5)
        self.assertEqual(calculadora.resta(-2,2),-4)
    def test_multi(self):
        self.assertEqual(calculadora.multiplicacion(4,3),12)
        self.assertEqual(calculadora.multiplicacion(0,5),0)
        self.assertEqual(calculadora.multiplicacion(-2,2),-4)
    def test_divisioon(self):
        self.assertEqual(calculadora.division(10,2),5)
        self.assertEqual(calculadora.division(7,3),7/3)
        with self.assertRaises(ValueError):
            calculadora.division(5,0)

if __name__ == '__main__':
    unittest.main()