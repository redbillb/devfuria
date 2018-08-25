# -*- coding: utf-8 -*-

#imports
import unittest


class Juros(object):
	pass


def minha_funcao(obj):
	return obj.capital * obj.taxa * obj.periodo


#Testes
class TestaJuros(unittest.TestCase):

	juros = Juros()
	juros.simples = minha_funcao

	def testaCalculoJuros(self):
		self.juros.capital = 16000
		self.juros.taxa    = 0.04
		self.juros.periodo = 4
		self.assertEqual(2560,self.juros.simples(self.juros))

if __name__ == '__main__':
	unittest.main()
