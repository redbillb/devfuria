# -*- coding: utf-8 -*-

#imports


#processamento
def contarStrings(string):
	resultado = 0
	for caractere in string:
		resultado += 1
	return resultado

#testes
assert 8 == contarStrings("Red Bill")
assert 0 == contarStrings("")