# -*- coding: utf-8 -*-

#imports
import unittest

#processamento
def bubbleSort(lista):
	
	for ciclos in range(len(lista) - 1):
		for indice in range(len(lista) - 1):
			if lista[indice] > lista[indice + 1]:
				lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
	return lista

#testes
class testeBubbleSort(unittest.TestCase):
	def testaOrdenar(self):
		self.assertEqual([1,3,5], bubbleSort([5,3,1]))
		self.assertEqual([0,1,2,3,4,5,6,7], bubbleSort([5, 3, 2, 4, 7, 1, 0, 6]))

if __name__ == '__main__':
	unittest.main()