# -*- coding: utf-8 -*-

#imports
import unittest

class Calc(object):
	def antecessor(numero):
		return numero - 1

	def sucessor(self,numero):
		return numero + 1


#testes
class TesteCalc(unittest.TestCase):

	calc = Calc();

	def testeAntecessor(self):
		self.assertEqual(4,Calc.antecessor(5))
		self.assertEqual(0,Calc.antecessor(1))
		self.assertNotEqual(5,Calc.antecessor(5))

	def testeSucessor(self):
		self.assertEqual(5,self.calc.sucessor(4))
		self.assertEqual(10,self.calc.sucessor(9))
		self.assertNotEqual(0,self.calc.sucessor(4))

if __name__ == '__main__':
	unittest.main()