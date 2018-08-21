# -*- coding: utf-8 -*-

#imports


#processamento
class Submarino:
	
	

	def __init__(self, X=0, Y=0, Z=0):
		self.X = X
		self.Y = Y
		self.Z = Z
		self.direcoes=['NORTE','LESTE','SUL','OESTE']
		self.indiceDirecoes = 0
		self.direcao = 'NORTE'

	def retornaPosicaoFinal(self,comandos):
		self.__init__()
		if comandos == '':
			#print ('aqui 1')
			return f'{self.X} {self.Y} {self.Z} {self.direcao}'
		else:
			#print (self.indiceDirecoes)
			for caractere in comandos:
				if caractere in ['R','L']:
					self.calculaDirecao(caractere)

				if caractere in ['U','D']:
					self.calcuDeslocamentoZ(caractere)

				if caractere == 'M':
					self.calculaAvanco()

			print (f'{self.X} {self.Y} {self.Z} {self.direcao}')
			return f'{self.X} {self.Y} {self.Z} {self.direcao}'
		#return '2 3 -2 SUL'

	def calculaDirecao(self,caractere):
		if caractere == 'L':
			#print ('aqui 3')
			self.indiceDirecoes += 1
		
		if caractere == 'R':
			self.indiceDirecoes -= 1
		
		if self.indiceDirecoes == -1:
			#print ('aqui 4')
			self.indiceDirecoes = 3

		if self.indiceDirecoes == 4:
			#print ('aqui 4')
			self.indiceDirecoes = 0
		
		self.direcao = self.direcoes[self.indiceDirecoes]
			
	def calcuDeslocamentoZ(self,caractere):
		if caractere == 'U':
			#print ('aqui 3')
			self.Z += 1
		
		if caractere == 'D':
			self.Z -= 1
		
	def calculaAvanco(self):
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
