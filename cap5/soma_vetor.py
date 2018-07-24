# -*- coding: utf-8 -*-

#imports


#processamento
def soma(vetor):
    resultado = 0
    for valor in vetor:
        resultado += valor
    return resultado

#testes
assert 60 == soma([10, 30, 5, 15, 0])
assert 15 == soma([15, 0])
assert 10 == soma([10])