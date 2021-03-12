def convertCelsiusToKelvin(celsius):
    ''' Kelvin = C + 273.15'''
    x = celsius + 273.15
    y = format(x, '.2f')
    return float(y)

def convertCelsiusToFahrenheit(celsius):
    ''' Fahrenheit = (C * 1.8) + 32'''
    x = celsius * 1.8 +32
    y = format(x, '.2f')
    return float(y)

def convertFahrenheitToCelsius(fahrenheit):
    ''' Celsius = (F-32) * .55'''
    x = (fahrenheit - 32) * .55
    y = format(x, '.2f')
    return float(y)

def convertFahrenheitToKelvin(fahrenheit):
    ''' Kelvin = (F + 459.67) * .55'''
    x = (fahrenheit + 459.67) * .55
    y = format(x, '.2f')
    return float(y)

def convertKelvinToCelsius(kelvin):
    ''' Celsius = K - 273.15'''
    x = (kelvin - 273.15)
    y = format(x, '.2f')
    return float(y)

def convertKelvinToFahrenheit(kelvin):
    ''' Fahrenheit = (K * 1.8) - 459.67'''
    x = (kelvin * 1.8) - 459.67
    y = format(x, '.2f')
    return float(y)

def main():
    print(convertCelsiusToKelvin(300))
    print(convertCelsiusToKelvin(200))
    print(convertCelsiusToKelvin(100))
    print(convertCelsiusToKelvin(0))
    print(convertCelsiusToKelvin(-10))
    print(type(convertCelsiusToKelvin(-10)))





if __name__ == '__main__':
    main()