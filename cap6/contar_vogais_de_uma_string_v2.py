# -*- coding: utf-8 -*-

#imports


#processamento
def contarVogais(string):
	vogais = 'aeiouAEIOU'
	resultado = 0
	for caractere in string:
		if caractere in vogais:
		   resultado += 1
	return resultado

#testes
assert 1 == contarVogais('Red')
assert 2 == contarVogais('Red Bill')
assert 2 == contarVogais('RED BILL')
assert 0 == contarVogais('kkk')