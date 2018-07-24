# -*- coding: utf-8 -*-

#imports


#processamento
def menor(vetor):
	indice = 0
	imenor = 0
	while indice < len(vetor):
		if vetor[imenor] > vetor[indice]:
			imenor = indice
		indice += 1
	return imenor

def maior(vetor):
	imaior = 0
	indice = 0
	while indice < len(vetor):
		if vetor[imaior] < vetor[indice]:
			imaior = indice
		indice += 1
	return imaior

#testes
assert 3 == menor([2,3,4,1])
assert 0 == menor([1,2,3,4])
assert 3 == menor([4,3,2,1])
assert 1 == menor([3,2])
assert 0 == menor([2])
assert 1 == menor([2,-3,4,1])

assert 2 == maior([2,3,4,1])
assert 3 == maior([1,2,3,4])
assert 0 == maior([4,3,2,1])
assert 0 == maior([3,2])
assert 0 == maior([2])
assert 2 == maior([2,-3,4,1])
