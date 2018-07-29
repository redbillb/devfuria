# -*- coding: utf-8 -*-

#imports


def inverterString(string):
    resultado = ""
    contador = 0
    while contador < len(string):
        resultado += string[(contador * -1) -1]
        contador += 1
    return resultado

#testes
assert "lamina" == inverterString("animal")
assert "deR" == inverterString("Red")