# -*- coding: utf-8 -*-

#imports


#entrada


#processamento
def ehPositivo(numero):
    if numero >= 0:
    	return True
    else:
    	return False

def ehNegativo(numero):
    if numero < 0:
    	return True
    else:
    	return False
	

#testes
assert ehPositivo(10)
assert not ehPositivo(-10)
assert ehNegativo(-10)
assert not ehNegativo(10)