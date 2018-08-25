# -*- coding: utf-8 -*-

#imports
import unittest


class Juros(object):
	pass




#Testes
class TestaJuros(unittest.TestCase):

	juros = Juros()
	juros.simples = lambda obj: obj.capital * obj.taxa * obj.periodo

	def testaCalculoJuros(self):
		self.juros.capital = 16000
		self.juros.taxa    = 0.04
		self.juros.periodo = 4
		self.assertEqual(2560,self.juros.simples(self.juros))

if __name__ == '__main__':
	unittest.main()
