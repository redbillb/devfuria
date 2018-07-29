# -*- coding: utf-8 -*-

#imports


#processamento
def compararDuasStrings(string1,string2):
    if len (string1) != len (string2):
        return False
    else:
        contador = 0
        while contador < len (string1):
            if string1[contador] != string2[contador]:
                return False
            contador += 1
    return True

#testes
assert compararDuasStrings("Red Bill","Red Bill")
assert not compararDuasStrings("Red Bill","Red BIll")
assert not compararDuasStrings("Red Bill","Red Bil")
assert not compararDuasStrings("Red Bil","Red Bill")
assert not compararDuasStrings("Red Bill","")