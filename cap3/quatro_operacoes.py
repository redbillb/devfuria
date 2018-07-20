# -*- coding: utf-8 -*-

#
#entrada
numero1 = 12
numero2 = 4

#processamento
def adicionar(numero1, numero2):
	return numero1 + numero2

def subtrair(numero1, numero2):
	return numero1 - numero2

def multiplicar(numero1, numero2):
	return numero1 * numero2

def dividir(numero1, numero2):
	return numero1 / numero2

#testes
assert 16 == adicionar(numero1, numero2)
assert 8  == subtrair(numero1, numero2)
assert 48 == multiplicar(numero1, numero2)
assert 3  == dividir(numero1, numero2)