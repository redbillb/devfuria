# -*- coding: utf-8 -*-

#imports
import unittest

#processamento
class Multiplos(object):
	
	def ehMultiploDe5(self,numero):
		if numero % 5 == 0:
			return True
		else:
			return False

	def ehMultiploDe3(self,numero):
		if numero % 3 == 0:
			return True
		else:
			return False

	def somaMultiplosDe_3_5(self,numero):
		resultado = 0
		for num in range(numero):
			if self.ehMultiploDe5(num) or self.ehMultiploDe3(num):
				resultado += num
		return resultado

#testes

multiplos = Multiplos()

class TestaMultiplos(unittest.TestCase):

	def testaEhMultiplode5(self):
		self.assertTrue(multiplos.ehMultiploDe5(5))
		self.assertTrue(multiplos.ehMultiploDe5(10))
		self.assertTrue(multiplos.ehMultiploDe5(15))

	def testaEhMultiploDe3(self):
		self.assertTrue(multiplos.ehMultiploDe3(3))
		self.assertTrue(multiplos.ehMultiploDe3(6))
		self.assertTrue(multiplos.ehMultiploDe3(15))

	def testaSomaMultiplosDe_3_5(self):
		self.assertEqual(23,multiplos.somaMultiplosDe_3_5(10))

if __name__ == '__main__':
	unittest.main()