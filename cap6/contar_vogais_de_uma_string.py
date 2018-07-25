# -*- coding: utf-8 -*-

#imports


#processamento
def contarVogais(string):
	resultado = 0
	for caractere in string:
		if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u' or \
		   caractere == 'A' or caractere == 'E' or caractere == 'I' or caractere == 'O' or caractere == 'U':
		   resultado += 1
	return resultado

#testes
assert 1 == contarVogais('Red')
assert 2 == contarVogais('Red Bill')
assert 0 == contarVogais('kkk')