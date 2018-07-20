# -*- coding: utf-8 -*-

#
#entrada

a = 999
b = 555

#processamento

temp = a
a = b
b = temp

#saida
assert a == 555
assert b == 999