# -*- coding: utf-8 -*-

#imports


#processamento
def ahDuplicidade(vetor):
    resultado = False
    contador = 0
    for elemento in vetor:
        contador += 1
        for indice in range(contador, len(vetor)):
            if vetor[indice] == elemento:
                resultado = True
    return resultado

#testes
assert ahDuplicidade([100, 200, 300, 300, 400])
assert not ahDuplicidade([100, 200, 300, 400])