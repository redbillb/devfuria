# -*- coding: utf-8 -*-

#imports


#processamento
def inverterString(string):
	resultado = ""
	for indice in range(len(string)):
		resultado += string[(indice * -1) -1]
	return resultado

#testes
assert "lamina" == inverterString("animal")
assert "deR" == inverterString("Red")