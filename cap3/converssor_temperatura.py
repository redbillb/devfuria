# -*- coding: utf-8 -*-

#
#entrada
celsius = 100
fahrenheit = 212

#processamento
def toCelsius(temperatura):
	return (temperatura - 32) / 9 * 5

def toFahrenheit(temperatura):
	return temperatura * 9 / 5 + 32
	
#testes
assert fahrenheit == toFahrenheit(celsius)
assert celsius    == toCelsius(fahrenheit)
