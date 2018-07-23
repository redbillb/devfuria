# -*- coding: utf-8 -*-

def divisores(numero):
    lista = []
    for contador in range(1, numero + 1):
    	if numero % contador == 0:
    		lista.append(contador)
    return lista
