# -*- coding: utf-8 -*-

#imports
import unittest

def encontraMaiorDivisivel(maximo):
    numero = maximo
    while True:
        contador = 0
        for valor in range(1,maximo + 1):
            
            if numero % valor == 0:
                contador += 1
            else:
                contador = 0
            if contador == maximo:
                return numero
            
        numero += 1

class testaDivisibilidade(unittest.TestCase):

	def testaEcontraMaiorDivisivel(self):
		self.assertEqual(2520,encontraMaiorDivisivel(10))

		print (encontraMaiorDivisivel(20))

if __name__ == '__main__':
	unittest.main()