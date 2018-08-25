# -*- coding: utf-8 -*-

#imports
import unittest

class Triangulo(object):
	def __init__(self,lado1,lado2,lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3


	def ehTriangulo(self):
		if self.lado1 > self.lado2 + self.lado3:
			return False
		elif self.lado2 > self.lado1 + self.lado3:
			return False
		elif self.lado3 > self.lado1 + self.lado1:
			return False
		else:
			return True

class testeTriangulo(unittest.TestCase):

	triangulo1 = Triangulo(3,4,5)

	def testeSeEhTriangulo(self):
		self.assertTrue(self.triangulo1.ehTriangulo())

	triangulo2 = Triangulo(1,4,5)

	def testeSeNaoEhTriangulo(self):
		self.assertFalse(self.triangulo2.ehTriangulo())

if __name__ == '__main__':
	unittest.main()