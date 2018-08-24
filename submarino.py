# -*- coding: utf-8 -*-

class Submarino:

	def __init__(self):
		self.X = 0
		self.Y = 0
		self.Z = 0
		self.direcao = 'NORTE'
		self.direcoes=['NORTE','LESTE','SUL','OESTE']

	def ressetaCoordenadas(self):
		self.__init__()
		return f'{self.X} {self.Y} {self.Z} {self.direcao}'

	def calculaCoordenada(self,comandos,resseta):
		if resseta:
			self.ressetaCoordenadas()
		for caractere in comandos:
			if caractere == 'L':
				self.calculaLEFT()

			elif caractere == 'R':
				self.calculaRIGTH()

			elif caractere == 'U':
				self.calculaUP()

			elif caractere == 'D':
				self.calculaDOWN()

			elif caractere == 'M':
				self.calculaAvanco()

			else:
				pass

		return f'{self.X} {self.Y} {self.Z} {self.direcao}'

	def calculaIndiceDirecaoAtual(self):
		for indice in range(len(self.direcoes)):
			if self.direcao == self.direcoes[indice]:
				return indice

	def calculaLEFT(self):
		indiceDirecoes = self.calculaIndiceDirecaoAtual() + 1
		indiceDirecoes = self.ajustaIndiceDirecoes(indiceDirecoes)
		self.direcao = self.direcoes[indiceDirecoes]
		return self.direcao

	def calculaRIGTH(self):
		indiceDirecoes = self.calculaIndiceDirecaoAtual() - 1
		indiceDirecoes = self.ajustaIndiceDirecoes(indiceDirecoes)
		self.direcao = self.direcoes[indiceDirecoes]
		return self.direcao

	def ajustaIndiceDirecoes(self,indice):
		if indice == -1:
			indice = 3

		if indice == 4:
			indice = 0

		return indice
		
	def calculaUP(self):
		if self.Z < 0:
			self.Z += 1
		return self.Z
		
	def calculaDOWN(self):
		self.Z -= 1
		return self.Z
		
	def calculaAvanco(self):
		if self.direcao == 'NORTE':
			self.Y += 1
			return self.Y
		
		if self.direcao == 'SUL':
			self.Y -= 1
			return self.Y

		if self.direcao == 'LESTE':
			self.X -= 1
			return self.X
		
		if self.direcao == 'OESTE':
			self.X += 1
			return self.X

#testes
#OBS: a cada teste a posição volta a ser a inicial

submarino = Submarino()
assert '0 0 0 NORTE' == submarino.calculaCoordenada('',True)
assert '0 0 0 NORTE' == submarino.calculaCoordenada('a',True)
assert '0 0 0 LESTE' == submarino.calculaCoordenada('L',True)
assert '0 0 0 OESTE' == submarino.calculaCoordenada('R',True)
assert '0 0 0 NORTE' == submarino.calculaCoordenada('U',True)
assert '0 0 -1 NORTE' == submarino.calculaCoordenada('D',True)
assert '0 0 -4 NORTE' == submarino.calculaCoordenada('DDDD',True)
assert '0 0 0 NORTE' == submarino.calculaCoordenada('DDDUUU',True)
assert '0 0 -2 NORTE' == submarino.calculaCoordenada('UUUUDD',True)
assert '0 1 0 NORTE' == submarino.calculaCoordenada('M',True)
assert '0 5 0 NORTE' == submarino.calculaCoordenada('MMMMM',True)
assert '0 -4 0 SUL' == submarino.calculaCoordenada('RRMMMM',True)
assert '0 0 0 NORTE' == submarino.calculaCoordenada('RRRR',True)
assert '0 0 0 NORTE' == submarino.calculaCoordenada('LLLL',True)

assert '2 3 -2 SUL' == submarino.calculaCoordenada('RMMLMMMDDLL',True)