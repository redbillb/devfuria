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

#testes
class TestaRecursao(unittest.TestCase):

    def testeCalculaFibonaci(self):

        self.assertEqual(0,calculaFibonaci(0))
        self.assertEqual(1,calculaFibonaci(1))
        self.assertEqual(1,calculaFibonaci(2))
        self.assertEqual(2,calculaFibonaci(3))
        self.assertEqual(3,calculaFibonaci(4))
        self.assertEqual(5,calculaFibonaci(5))
        self.assertEqual(8,calculaFibonaci(6))

if __name__ == '__main__':
    unittest.main()