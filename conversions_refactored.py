import unittest
from conversions import *

class ConversionNotPossible(Exception):
   pass

def convert(fromUnit, toUnit, value):

    if fromUnit == "C" and toUnit == "K":
        # convert Celsius to Kelvin
        return convertCelsiusToKelvin(value)

    elif fromUnit == "C" and toUnit == "F":
        # convert Celsius to Fahrenheit
        return convertCelsiusToFahrenheit(value)

    elif fromUnit == "F" and toUnit == "C":
        #convert Fahrenheit to Celsius
        return convertFahrenheitToCelsius(value)

    elif fromUnit == "F" and toUnit == "K":
        #convert Fahrenheit to Kelvin
        return convertFahrenheitToKelvin(value)

    elif fromUnit == "K" and toUnit == "C":
        #convert Kelvin to Celsius
        return convertKelvinToCelsius(value)

    elif fromUnit == "K" and toUnit == "F":
        #convert Kelvin to Fahrenheit
        return convertKelvinToFahrenheit(value)

     #**********   length conversions below  *********

    elif fromUnit == "m" and toUnit == "Y":
        #convert Meter to Yards
        return convertMetersToYards(value)

    elif fromUnit == "Y" and toUnit == "m":
        # convert meter to yards
        return convertYardsToMeters(value)

    elif fromUnit == "m" and toUnit == "M":
        #convert Meters to Miles
        return convertMetersToMiles(value)

    elif fromUnit == "M" and toUnit == "m":
        #convert Miles to Meters
        return convertMilesToMeters(value)

    elif fromUnit == "Y" and toUnit == "M":
        #convert Yards to Miles
        return convertYardsToMiles(value)

    elif fromUnit == "M" and toUnit == "Y":
        #convert Miles to Yards
        return convertMilesToYards(value)

    if (fromUnit == "C" or "K" or "F") and (toUnit != "C" or "K" or "F"):
        raise ConversionNotPossible('Units will not convert. Try different units instead.')
    elif (fromUnit == "m" or "M" or "Y") and (toUnit != "m" or "M" or "Y"):
        raise ConversionNotPossible('Units will not convert. Try different units instead.')








