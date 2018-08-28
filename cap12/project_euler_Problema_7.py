# -*- coding: utf-8 -*-

#imports
import unittest


def ehPrimo(numero):
   listaDivisores = []
   for num in range(1,numero + 1):
       if numero % num == 0:
           listaDivisores.append(num)
   if len(listaDivisores) > 2 or numero == 1:
       return False
   return True 


def encontraPrimoNaPosicaoIndicada(posicao_final):
    numero = 2
    posicao_inicial = 1
    while True:
        if ehPrimo(numero):
            if posicao_inicial == posicao_final:
                return numero
            posicao_inicial += 1
            #print(posicao_inicial)
        numero += 1


class TestaPrimos(unittest.TestCase):

    def testaEhPrimo(self):
        self.assertFalse(ehPrimo(1))
        self.assertTrue(ehPrimo(3))
        self.assertTrue(ehPrimo(5))
        self.assertTrue(ehPrimo(7))
        self.assertTrue(ehPrimo(13))
        self.assertTrue(ehPrimo(29))
        self.assertFalse(ehPrimo(4))
        self.assertFalse(ehPrimo(25))

    def testaEncontraPrimoNaPosicaoIndicada(self):
        
        self.assertEqual(13,encontraPrimoNaPosicaoIndicada(6))
       
        print(encontraPrimoNaPosicaoIndicada(10001))

if __name__ == '__main__':
    unittest.main()
