# -*- coding: utf-8 -*-

#imports
import unittest

def calculaFibonaci(numero):
        lista = []
        indice = -1
        while indice < numero:
            indice += 1
            if indice == 0:
                lista.append(indice)
            elif indice == 1:
                lista.append(indice)
            else:
                lista.append(lista[indice-1]+lista[indice-2])
                
        return lista[numero]

def criaListaFibonaci(numero,quantidade):
    lista = []
    for num in range(numero + 1):
        elemento = calculaFibonaci(num)
        if elemento < numero + 1 and elemento % 2 == 0:
            lista.append(elemento)
        if quantidade == 0:
            if elemento > numero + 1:
                break
        else:
            if elemento > numero + 1 or len(lista) >= quantidade:
                break
    return lista

class TestaRecursao(unittest.TestCase):

    def testeCalculaFibonaci(self):

        self.assertEqual(0,calculaFibonaci(0))
        self.assertEqual(1,calculaFibonaci(1))
        self.assertEqual(1,calculaFibonaci(2))
        self.assertEqual(2,calculaFibonaci(3))
        self.assertEqual(3,calculaFibonaci(4))
        self.assertEqual(5,calculaFibonaci(5))
        self.assertEqual(8,calculaFibonaci(6))

    def testaCriaListaFibonaci(self):
        self.assertEqual([0, 2, 8, 34],criaListaFibonaci(4000000,4))
        print (sum(criaListaFibonaci(4000000,0)))

if __name__ == '__main__':
    unittest.main()
    