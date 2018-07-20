# -*- coding: utf-8 -*-

#
#entrada

capital = 16000
taxa = .04
periodo = 4

#processamento
def juros_simples(capital, taxa, periodo):
    return capital * taxa * periodo

#saida
assert 2560 == juros_simples(capital, taxa, periodo)