# -*- coding: utf-8 -*-

#imports


#processamento
def compararDuasStrings(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        for indice in range(len(string1)):
            if string1[indice] != string2[indice]:
                return False
    return True

#testes
assert compararDuasStrings("Red Bill","Red Bill")
assert not compararDuasStrings("Red Bill","Red BIll")
assert not compararDuasStrings("Red Bill","Red Bil")
assert not compararDuasStrings("Red Bil","Red Bill")
assert not compararDuasStrings("Red Bill","")
