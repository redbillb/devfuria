# -*- coding: utf-8 -*-

#imports
import unittest


#processamento

class Area(object):
	def areaQuadrada(self,numero):
		return numero * numero

	def areaCubica(self,numero):
		return numero * numero * numero


#Testes

class testeAreas(unittest.TestCase):

	area = Area()

	def testeAreaQuadrada(self):
		self.assertEqual(16,self.area.areaQuadrada(4))
		self.assertEqual(25,self.area.areaQuadrada(5))
		self.assertNotEqual(17,self.area.areaQuadrada(4))

	def testeAreaCubica(self):
		self.assertEqual(8,self.area.areaCubica(2))
		self.assertEqual(27,self.area.areaCubica(3))
		self.assertNotEqual(9,self.area.areaCubica(2))

if __name__ == '__main__':
	unittest.main()