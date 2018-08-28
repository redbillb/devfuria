# -*- coding: utf-8 -*-

#imports
import unittest

#processamento
class Multiplos(object):
	
	def ehMultiplo(self,numero,multiplo):
		if numero % multiplo == 0:
			return True
		return False

	def somaMultiplosDe_3_5(self,numero):
		resultado = 0
		for num in range(numero):
			if self.ehMultiplo(num,3) or self.ehMultiplo(num,5):
				resultado += num
		return resultado

#testes

multiplos = Multiplos()

class TestaMultiplos(unittest.TestCase):

	def testaEhMultiplode5(self):
		self.assertTrue(multiplos.ehMultiplo(5,5))
		self.assertTrue(multiplos.ehMultiplo(10,5))
		self.assertTrue(multiplos.ehMultiplo(15,5))

	def testaEhMultiploDe3(self):
		self.assertTrue(multiplos.ehMultiplo(3,3))
		self.assertTrue(multiplos.ehMultiplo(6,3))
		self.assertTrue(multiplos.ehMultiplo(15,3))

	def testaSomaMultiplosDe_3_5(self):
		self.assertEqual(23,multiplos.somaMultiplosDe_3_5(10))
		self.assertEqual(78,multiplos.somaMultiplosDe_3_5(20))

	print (multiplos.somaMultiplosDe_3_5(1000))

if __name__ == '__main__':
	unittest.main()