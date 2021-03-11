def convertCelsiusToKelvin(celsius):
    ''' Kelvin = C + 273.15'''
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    ''' Celsius * 1.8 + 32'''
    return celsius * 1.8 +32

def main():
    print(convertCelsiusToKelvin(300))
    print(convertCelsiusToKelvin(200))
    print(convertCelsiusToKelvin(100))
    print(convertCelsiusToKelvin(0))
    print(convertCelsiusToKelvin(-100))

    print(convertCelsiusToFahrenheit(300))
    print(convertCelsiusToFahrenheit(200))
    print(convertCelsiusToFahrenheit(100))
    print(convertCelsiusToFahrenheit(0))
    print(convertCelsiusToFahrenheit(-100))


if __name__ == '__main__':
    main()