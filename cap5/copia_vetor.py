# -*- coding: utf-8 -*-

#imports


#processamento
def copiaVetor(vetor):
	saida = []
	for elemento in vetor:
		saida.append(elemento)
	return saida

#testes
assert [10, 20, 30, 0] == copiaVetor([10, 20, 30, 0])
