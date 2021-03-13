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

def convertMetersToYards(Meter):
    ''' Yard = Meter * 1.0936'''

    x = Meter * 1.0936
    y = format(x, '.2f')
    return float(y)

def convertYardsToMeters(Yard):
    ''' Meter = Yard/1.0936 '''

    x = Yard/1.0936
    y = format(x, '.2f')
    return float(y)

def convertMetersToMiles(Meter):
    ''' Mile = Meter * 0.00062137 '''

    x = Meter * 0.00062137
    y = format(x, '.2f')
    return float(y)

def convertMilesToMeters(Mile):
    ''' Meter = Mile/.00062137 '''

    x = Mile/.00062137
    y = format(x, '.2f')
    return float(y)

def convertYardsToMiles(Yard):
    ''' Miles = Yard * .00056818 '''

    x = Yard * .00056818
    y = format(x, '.2f')
    return float(y)

def convertMilesToYards(Mile):
    ''' Yard = Mile * 1760 '''

    x = Mile * 1760
    y = format(x, '.2f')
    return float(y)

def main():
    print(convertMilesToYards(10))
    print(convertMilesToYards(100))






if __name__ == '__main__':
    main()