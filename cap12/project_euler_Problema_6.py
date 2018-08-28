# -*- coding: utf-8 -*-

#imports
import unittest


def calculaSomaDosQuadrados(numero):
	resultado = 0
	for num in range(1,numero + 1):
		resultado += num * num
	return resultado

def calculaQuadradoDasoma(numero):
	resultado = 0
	for num in range(1,numero + 1):
		resultado += num
	return resultado * resultado

def calculaDiferencaDosQuadrados(numero):
	return calculaQuadradoDasoma(numero) - calculaSomaDosQuadrados(numero)


class testaCalculos(unittest.TestCase):
	def testaCalculaSomaDosQuadrados(self):
		self.assertEqual(385,calculaSomaDosQuadrados(10))

	def testaCalculaQuadradoDasoma(self):
		self.assertEqual(3025,calculaQuadradoDasoma(10))

	def testaCalculaDiferencaDosQuadrados(self):
		self.assertEqual(2640,calculaDiferencaDosQuadrados(10))

		print(calculaDiferencaDosQuadrados(100))


if __name__ == '__main__':
	unittest.main()
