# -*- coding: utf-8 -*-

#imports


#processamento
def contarStrings(string):
	resultado = 0
	contador = 0
	while contador < len(string):
		resultado += 1
		contador += 1
	return resultado

#testes
assert 8 == contarStrings("Red Bill")
assert 0 == contarStrings("")