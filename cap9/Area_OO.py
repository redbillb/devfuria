# -*- coding: utf-8 -*-

#imports
import unittest


#processamento

class Area(object):
	def areaQuadrada(self,numero1,numero2):
		return numero1 * numero2

	def areaCubica(self,numero1,numero2,numero3):
		return numero1 * numero2 * numero3

#Testes

class testeAreas(unittest.TestCase):

	area = Area()

	def testeAreaQuadrada(self):
		self.assertEqual(16,area.areaQuadrada(4,4))
		self.assertEqual(25,self.area.areaQuadrada(5,5))
		self.assertNotEqual(17,self.area.areaQuadrada(4,3))

	def testeAreaCubica(self):
		self.assertEqual(8,self.area.areaCubica(2,2,2))
		self.assertEqual(27,self.area.areaCubica(3,3,3))
		self.assertNotEqual(9,self.area.areaCubica(2,3,4))

if __name__ == '__main__':
	unittest.main()