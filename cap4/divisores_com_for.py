# -*- coding: utf-8 -*-

#imports


#processamento
def divisores(numero):
    lista = []
    for contador in range(1, numero + 1):
    	if numero % contador == 0:
    		lista.append(contador)
    return lista


#testes
assert [1, 2] == divisores(2)
assert [1, 2, 5, 10] == divisores(10)
assert [1, 2, 3, 4, 6, 12] == divisores(12)
