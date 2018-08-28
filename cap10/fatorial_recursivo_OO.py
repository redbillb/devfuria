# -*- coding: utf-8 -*-

#imports
import unittest

#processamento

def calculaFatorial(numero):
	if numero == 0:
		return 0
	elif numero == 1:
		return 1
	else:
		return numero * calculaFatorial(numero - 1)

#testes
class TestaRecursividade(unittest.TestCase):
	def testaCalculaFatorial(self):
		self.assertEqual(1,calculaFatorial(1))
		self.assertEqual(2,calculaFatorial(2))
		self.assertEqual(6,calculaFatorial(3))
		self.assertEqual(24,calculaFatorial(4))
		self.assertNotEqual(2,calculaFatorial(1))

if __name__ == '__main__':
	unittest.main()
