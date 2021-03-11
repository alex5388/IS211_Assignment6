import unittest
from conversions import *


class TestConversion(unittest.TestCase):

    def test_CelsiusToKelvin(self):
        '''test celsius to kelvin conversion function '''
        self.assertEqual(convertCelsiusToKelvin(300), 573.15)
        self.assertEqual(convertCelsiusToKelvin(200), 473.15)
        self.assertEqual(convertCelsiusToKelvin(100), 373.15)
        self.assertEqual(convertCelsiusToKelvin(0), 273.15)
        #self.assertEqual(convertCelsiusToKelvin(-100), 173.14)


    def test_CelsiustoFahrenheit(self):
        '''test celsius to  function'''
        self.assertEqual(convertCelsiusToFahrenheit(300), 572.00)
        self.assertEqual(convertCelsiusToFahrenheit(200), 392.00)
        self.assertEqual(convertCelsiusToFahrenheit(100), 212.00)
        self.assertEqual(convertCelsiusToFahrenheit(0), 32.00)
        self.assertEqual(convertCelsiusToFahrenheit(-100), -148.00)


if __name__ == '__main__':
    unittest.main()
