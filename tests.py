import unittest
from conversions import *


class TestConversion(unittest.TestCase):

    def test_CelsiusToKelvin(self):
        '''Celsius to kelvin check '''
        self.assertEqual(convertCelsiusToKelvin(300), 573.15, 'Test 300')
        self.assertEqual(convertCelsiusToKelvin(200), 473.15, 'Test 200')
        self.assertEqual(convertCelsiusToKelvin(100), 373.15, 'Test 100')
        self.assertEqual(convertCelsiusToKelvin(0), 273.15, 'Test 0')
        self.assertEqual(convertCelsiusToKelvin(-10), 263.15, 'Test -10')


    def test_CelsiusToFahrenheit(self):
        '''Celsius to Fahrenheit check'''

        self.assertEqual(convertCelsiusToFahrenheit(300), 572.00, 'Test 300')
        self.assertEqual(convertCelsiusToFahrenheit(200), 392.00, 'Test 200')
        self.assertEqual(convertCelsiusToFahrenheit(100), 212.00, 'Test 100')
        self.assertEqual(convertCelsiusToFahrenheit(0), 32.00, 'Test 0')
        self.assertEqual(convertCelsiusToFahrenheit(-10), 14.00, 'Test -10')

    def test_FahrenheitToCelsius(self):
        '''Fahrenheit to Celsius check'''

        self.assertEqual(convertFahrenheitToCelsius(300), 147.40, 'Test 300')
        self.assertEqual(convertFahrenheitToCelsius(200), 92.40, 'Test 200')
        self.assertEqual(convertFahrenheitToCelsius(100), 37.40, 'Test 100')
        self.assertEqual(convertFahrenheitToCelsius(0), -17.60, 'Test 0')
        self.assertEqual(convertFahrenheitToCelsius(-10), -23.10, 'Test -10')

    def test_FahrenheitToKelvin(self):
        '''Fahrenheit to Kelvin check'''

        self.assertEqual(convertFahrenheitToKelvin(300), 417.82, 'Test 300')
        self.assertEqual(convertFahrenheitToKelvin(200), 362.82, 'Test 200')
        self.assertEqual(convertFahrenheitToKelvin(100), 307.82, 'Test 100')
        self.assertEqual(convertFahrenheitToKelvin(0), 252.82, 'Test 0')
        self.assertEqual(convertFahrenheitToKelvin(-10), 247.32, 'Test -10')

    def test_KelvinToCelsius(self):
        '''Kelvin to Celsius check'''

        self.assertEqual(convertKelvinToCelsius(300), 26.85, 'Test 300')
        self.assertEqual(convertKelvinToCelsius(200), -73.15, 'Test 200')
        self.assertEqual(convertKelvinToCelsius(100), -173.15, 'Test 100')
        self.assertEqual(convertKelvinToCelsius(0), -273.15, 'Test 0')
        self.assertEqual(convertKelvinToCelsius(-10), -283.15, 'Test -10')

    def test_KelvinToFahrenheit(self):
        '''Kelvin to Fahrenheit check'''

        self.assertEqual(convertKelvinToFahrenheit(300), 80.33, 'Test 300')
        self.assertEqual(convertKelvinToFahrenheit(200), -99.67, 'Test 200')
        self.assertEqual(convertKelvinToFahrenheit(100), -279.67, 'Test 100')
        self.assertEqual(convertKelvinToFahrenheit(0), -459.67, 'Test 0')
        self.assertEqual(convertKelvinToFahrenheit(-10), -477.67, 'Test -10')


if __name__ == '__main__':
    unittest.main()
