# -*- coding: utf-8 -*-

class Submarino:

	def __init__(self):
		self.X = 0
		self.Y = 0
		self.Z = 0
		self.direcao = 'NORTE'
		self.__indiceDirecoes = 0

	def retornaPosicaoFinal(self,comandos):
		self.__init__()

		for caractere in comandos:
			if caractere in ['R','L']:
				self.__calculaDirecao(caractere)

			elif caractere in ['U','D']:
				self.__calcuDeslocamentoZ(caractere)

			elif caractere == 'M':
				self.__calculaAvanco()

			else:
				pass

		return f'{self.X} {self.Y} {self.Z} {self.direcao}'

	def __calculaDirecao(self,caractere):
		direcoes=['NORTE','LESTE','SUL','OESTE']
		
		if caractere == 'L':
			self.__indiceDirecoes += 1
		
		if caractere == 'R':
			self.__indiceDirecoes -= 1
		
		if self.__indiceDirecoes == -1:
			self.__indiceDirecoes = 3

		if self.__indiceDirecoes == 4:
			self.__indiceDirecoes = 0
		
		self.direcao = direcoes[self.__indiceDirecoes]
			
	def __calcuDeslocamentoZ(self,caractere):
		if caractere == 'U':
			self.Z += 1
		
		if caractere == 'D':
			self.Z -= 1
		
	def __calculaAvanco(self):
		if self.direcao == 'NORTE':
			self.Y += 1
		
		if self.direcao == 'SUL':
			self.Y -= 1
		
		if self.direcao == 'LESTE':
			self.X -= 1
		
		if self.direcao == 'OESTE':
			self.X += 1

#testes
#OBS: a cada teste a posição volta a ser a inicial

submarino = Submarino()
assert '0 0 0 NORTE' == submarino.retornaPosicaoFinal('')
assert '0 0 0 NORTE' == submarino.retornaPosicaoFinal('a')
assert '0 0 0 LESTE' == submarino.retornaPosicaoFinal('L')
assert '0 0 0 OESTE' == submarino.retornaPosicaoFinal('R')
assert '0 0 1 NORTE' == submarino.retornaPosicaoFinal('U')
assert '0 0 -1 NORTE' == submarino.retornaPosicaoFinal('D')
assert '0 0 -4 NORTE' == submarino.retornaPosicaoFinal('DDDD')
assert '0 0 3 NORTE' == submarino.retornaPosicaoFinal('UUU')
assert '0 0 3 NORTE' == submarino.retornaPosicaoFinal('UUUUUDD')
assert '0 1 0 NORTE' == submarino.retornaPosicaoFinal('M')
assert '0 5 0 NORTE' == submarino.retornaPosicaoFinal('MMMMM')
assert '0 -4 0 SUL' == submarino.retornaPosicaoFinal('RRMMMM')
assert '0 0 0 NORTE' == submarino.retornaPosicaoFinal('RRRR')
assert '0 0 0 NORTE' == submarino.retornaPosicaoFinal('LLLL')

assert '2 3 -2 SUL' == submarino.retornaPosicaoFinal('RMMLMMMDDLL')