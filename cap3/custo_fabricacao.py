# -*- coding: utf-8 -*-

#imports


#entrada
custo_de_fabrica = 10000

#processamento
def calculoCustoFinal(custo):
	#Regra de negocio
    percentual_distribuidor = .28
    percentual_impostos = .45

    return custo * percentual_impostos + custo * percentual_distribuidor + custo
	
#testes
custo_final = 17300

assert custo_final == calculoCustoFinal(custo_de_fabrica)
