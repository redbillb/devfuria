# -*- coding: utf-8 -*-

#imports


#processamento
contador = 1
vetor = []
while contador < 6:
    vetor.append(contador)
    contador += 1

#testes
assert 1 == vetor[0]
assert 2 == vetor[1]
assert 3 == vetor[2]
assert 4 == vetor[3]
assert 5 == vetor[4]