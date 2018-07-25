# -*- coding: utf-8 -*-

#imports


#processamento
def ahDuplicidade(vetor):
    return len(vetor) != len(set(vetor))

#testes
assert ahDuplicidade([100, 200, 300, 300, 400])
assert not ahDuplicidade([100, 200, 300, 400])