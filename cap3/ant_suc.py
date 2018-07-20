# -*- coding: utf-8 -*-

#
#entrada
teste_numero = 10

#processamento
def antecessor(numero):
	return numero - 1

def sucessor(numero):
	return numero + 1

#testes
assert 11 == sucessor(teste_numero)
assert 9 == antecessor(teste_numero)