# -*- coding: utf-8 -*-

#imports
import unittest

#processamento
class Calculadora(object):
	def calculaDobro(self,numero):
		return numero * 2

#testes

class TesteCalculadora(unittest.TestCase):

	calculadora = Calculadora()

	def testeCalculaDobro(self):
		self.assertEqual(4,self.calculadora.calculaDobro(2))
		self.assertEqual(10,self.calculadora.calculaDobro(5))
		self.assertNotEqual(5,self.calculadora.calculaDobro(2))

if __name__ == '__main__':
	unittest.main()