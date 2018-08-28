# -*- coding: utf-8 -*-

#imports
import unittest

def ehPalindromo(numero):
    lista = []
    for caractere in str(numero):
        lista.append(caractere)

    listaInv = lista[::-1]
    
    for indice in range(len(lista)):
        if lista[indice] != listaInv[indice]:
            return False
    return True

def encontraMaiorPalindromo2Dig():
    lista = []
    for x in range(100)[::-1]:
        #print(x)
        for y in range(100)[::-1]:
            elemento = x * y
            if ehPalindromo(elemento):
                lista.append(elemento)
                #print (elemento)
    return max(lista)

def encontraMaiorPalindromo3Dig():
    lista = []
    for x in range(1000)[::-1]:
        #print(x)
        for y in range(1000)[::-1]:
            elemento = x * y
            if ehPalindromo(elemento):
                lista.append(elemento)
                #print (elemento)
    return max(lista)

class testaPalindromo(unittest.TestCase):
    
    def testaSeNumeroEhPalindromo(self):
        self.assertTrue(ehPalindromo(202))
        self.assertTrue(ehPalindromo(9009))
        self.assertFalse(ehPalindromo(203))

    def testaEncontraMaiorPalindromo(self):
        self.assertEqual(9009,encontraMaiorPalindromo2Dig())

        print (encontraMaiorPalindromo3Dig())


if __name__ == '__main__':
    unittest.main()
