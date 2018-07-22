# -*- coding: utf-8 -*-

#imports


#entrada


#processamento
def isPar(numero):
    if numero % 2 == 0:
    	return True
    else:
        return False
	
#testes
assert True == isPar(10)
assert False == isPar(11)