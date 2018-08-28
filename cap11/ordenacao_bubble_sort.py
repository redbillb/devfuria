# -*- coding: utf-8 -*-

#imports
import unittest

#processamento
def bubbleSort(lista):
	qtd = len(lista) - 1
	for ciclos in range(len(lista) - 1):
		for indice in range(qtd):
			#print (indice, end='')
			if lista[indice] > lista[indice + 1]:
				if indice + 1 == qtd:
					qtd -= 1
				lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
			#print ('   ', end='')
		#print ()
	return lista

#testes
class testeBubbleSort(unittest.TestCase):
	def testaOrdenar(self):
		self.assertEqual([1,3,5], bubbleSort([5,3,1]))
		self.assertEqual([0,1,2,3,4,5,6,7], bubbleSort([5, 3, 2, 4, 7, 1, 0, 6]))
		self.assertEqual([0,10,20,30,40,50,60,70], bubbleSort([50, 30, 20, 40, 70, 10, 0, 60]))
		self.assertEqual([0,10,20,30,40,50,60,70], bubbleSort([70, 30, 20, 40, 50, 10, 60, 0]))

if __name__ == '__main__':
	unittest.main()