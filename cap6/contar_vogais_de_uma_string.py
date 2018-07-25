# -*- coding: utf-8 -*-

#imports


#processamento
def contaVogais(string):
	resultado = 0
	for caractere in string:
		if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u' or \
		   caractere == 'A' or caractere == 'E' or caractere == 'I' or caractere == 'O' or caractere == 'U':
		   resultado += 1
	return resultado

#testes
assert 1 == contaVogais('Red')
assert 2 == contaVogais('Red Bill')
assert 0 == contaVogais('kkk')