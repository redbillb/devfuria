# -*- coding: utf-8 -*-

#imports
import unittest

class Exec(object):
    def __init__(self):
        self.lista = []

    def ehPrimo(self,numero):
        listaDivisores = []
        for num in range(1,numero + 1):
            if numero % num == 0:
                listaDivisores.append(num)
        if len(listaDivisores) > 2 or numero == 1:
            return False
        return True 
    
    def looping(self,numero):
        if len(self.lista) == 0:
            inicio = 2
        else:
            inicio = max(self.lista)
        for num in range(inicio,numero + 1):
            if numero % num == 0:
                self.lista.append(num)
                return int (numero / num)
    
    def criaListaPrimos(self,numero):
        self.__init__()
        while numero > 1:
            numero = self.looping(numero)

        lista2 = []

        for item in self.lista:
            if self.ehPrimo(item):
                lista2.append(item)
        return lista2

teste = Exec()

class TestaPrimos(unittest.TestCase):

    def testaEhPrimo(self):
        self.assertFalse(teste.ehPrimo(1))
        self.assertTrue(teste.ehPrimo(3))
        self.assertTrue(teste.ehPrimo(5))
        self.assertTrue(teste.ehPrimo(7))
        self.assertTrue(teste.ehPrimo(13))
        self.assertTrue(teste.ehPrimo(29))
        self.assertFalse(teste.ehPrimo(4))
        self.assertFalse(teste.ehPrimo(25))

    def testaCriaListaPrimos(self):
        
        self.assertEqual([2,5],teste.criaListaPrimos(10))
        
        self.assertEqual([5, 7, 13, 29],teste.criaListaPrimos(13195))

        self.assertEqual(29,max(teste.criaListaPrimos(13195)))
        
        print (max(teste.criaListaPrimos(600851475143)))

if __name__ == '__main__':
    unittest.main()
