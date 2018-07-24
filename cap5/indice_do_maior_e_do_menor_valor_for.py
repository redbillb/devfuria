# -*- coding: utf-8 -*-

#imports


#processamento
def menor(vetor):
	menor = vetor[0]
	for indice in range(1,len(vetor)):
		if menor > vetor[indice]:
			menor = vetor[indice]
	return menor

def maior(vetor):
	maior = vetor[0]
	for indice in range(1,len(vetor)):
		if maior < vetor[indice]:
			maior = vetor[indice]
	return maior

#testes
assert 1 == menor([2,3,4,1])
assert 1 == menor([1,2,3,4])
assert 1 == menor([4,3,2,1])
assert 2 == menor([3,2])
assert 2 == menor([2])
assert -3 == menor([2,-3,4,1])

assert 4 == maior([2,3,4,1])
assert 4 == maior([1,2,3,4])
assert 4 == maior([4,3,2,1])
assert 3 == maior([3,2])
assert 2 == maior([2])
assert 4 == maior([2,-3,4,1])