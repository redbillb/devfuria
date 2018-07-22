# -*- coding: utf-8 -*-
from math import sqrt
#
#entrada
a = 1
b = 0
c = -16

#processamento
def calculoDelta(a,b,c):
	return b ** 2 - 4 * a * c

def calculoRaiz1(a,b,c):
	return (-1 * b - sqrt(calculoDelta(a,b,c))) / 2 * a

def calculoRaiz2(a,b,c):
	return (-1 * b + sqrt(calculoDelta(a,b,c))) / 2 * a
	
#testes
delta = 64
raiz1 = -4
raiz2 = 4

assert delta == calculoDelta(a,b,c)
assert raiz1 == calculoRaiz1(a,b,c)
assert raiz2 == calculoRaiz2(a,b,c)
