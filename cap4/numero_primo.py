# -*- coding: utf-8 -*-

#imports


#processamento
def divisores(numero):
    lista = []
    for contador in range(1, numero + 1):
    	if numero % contador == 0:
    		lista.append(contador)
    return lista


def ehPrimo(numero):
    lista = divisores(numero)
    if len(lista) == 2:
        return lista

#testes
assert ehPrimo(5)
assert not ehPrimo(4)
assert ehPrimo(97)
