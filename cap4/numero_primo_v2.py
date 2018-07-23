# -*- coding: utf-8 -*-

#imports
from meu_modulo import divisores

#processamento
def ehPrimo(numero):
    listaDeDivisores = divisores(numero)
    if len(listaDeDivisores) == 2:
        return True
    else:
    	return False

#testes
assert ehPrimo(2)
assert ehPrimo(3)
assert ehPrimo(5)
assert ehPrimo(7)
assert ehPrimo(11)
assert ehPrimo(13)
assert ehPrimo(17)
assert ehPrimo(19)
assert ehPrimo(23)

assert not ehPrimo(0)
assert not ehPrimo(1)
assert not ehPrimo(4)
assert not ehPrimo(6)
assert not ehPrimo(8)
assert not ehPrimo(9)
assert not ehPrimo(10)
assert not ehPrimo(12)
assert not ehPrimo(14)
assert not ehPrimo(15)
assert not ehPrimo(16)
assert not ehPrimo(18)

assert not ehPrimo(-2)
assert not ehPrimo(-4)