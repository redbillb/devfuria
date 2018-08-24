# -*- coding: utf-8 -*-
import unittest

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
        indiceDirecoes = self.calculaIndiceDirecaoAtual() - 1
        indiceDirecoes = self.ajustaIndiceDirecoes(indiceDirecoes)
        self.direcao = self.direcoes[indiceDirecoes]
        return self.direcao

    def calculaRIGTH(self):
        indiceDirecoes = self.calculaIndiceDirecaoAtual() + 1
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
            self.X += 1
            return self.X
        
        if self.direcao == 'OESTE':
            self.X -= 1
            return self.X

#testes

submarino = Submarino()

class TestSubmarino(unittest.TestCase):
    
    def testeSugeridoNoEnunciado(self):
        self.assertEqual(
            '2 3 -2 SUL',submarino.calculaCoordenada('RMMLMMMDDLL',True)
            )

        self.assertEqual(
            '-1 2 0 NORTE',submarino.calculaCoordenada('LMRDDMMUU',True)
            )

    # 
    #      NORTE
    #        0
    #
    #
    #OESTE         LESTE
    #  3             1
    #
    #
    #       2
    #      SUL
    #
    #  NORTE - SUL eixo Y
    #  OESTE - LESTE eixo X


    def testeDeRotacao(self):
        submarino.ressetaCoordenadas()
        self.assertEqual('NORTE', submarino.direcao)
        self.assertEqual('OESTE', submarino.calculaLEFT())
        self.assertEqual('NORTE', submarino.calculaRIGTH())
        self.assertEqual('LESTE', submarino.calculaRIGTH())
        self.assertEqual('SUL', submarino.calculaRIGTH())


    def testeDeProfundidade(self):
        submarino.ressetaCoordenadas()
        self.assertEqual(0, submarino.Z)
        self.assertEqual(0, submarino.calculaUP())
        self.assertEqual(-1, submarino.calculaDOWN())
        self.assertEqual(-2, submarino.calculaDOWN())
        self.assertEqual(-3, submarino.calculaDOWN())
        self.assertEqual(-2, submarino.calculaUP())


    def testeCalculaAvancoNORTE(self):
        submarino.ressetaCoordenadas()
        submarino.direcao = 'NORTE'
        submarino.calculaAvanco()
        self.assertEqual(0, submarino.X)
        self.assertEqual(1, submarino.Y)
        submarino.calculaAvanco()
        self.assertEqual(0, submarino.X)
        self.assertEqual(2, submarino.Y)


    def testeCalculaAvancoSUL(self):
        submarino.ressetaCoordenadas()
        submarino.direcao = 'SUL'
        submarino.calculaAvanco()
        self.assertEqual(0, submarino.X)
        self.assertEqual(-1, submarino.Y)
        submarino.calculaAvanco()
        self.assertEqual(0, submarino.X)
        self.assertEqual(-2, submarino.Y)


    def testeCalculaAvancoLESTE(self):
        submarino.ressetaCoordenadas()
        submarino.direcao = 'LESTE'
        submarino.calculaAvanco()
        self.assertEqual(1, submarino.X)
        self.assertEqual(0, submarino.Y)
        submarino.calculaAvanco()
        self.assertEqual(2, submarino.X)
        self.assertEqual(0, submarino.Y)


    def testeCalculaAvancoOESTE(self):
        submarino.ressetaCoordenadas()
        submarino.direcao = 'OESTE'
        submarino.calculaAvanco()
        self.assertEqual(-1, submarino.X)
        self.assertEqual(0, submarino.Y)
        submarino.calculaAvanco()
        self.assertEqual(-2, submarino.X)
        self.assertEqual(0, submarino.Y)


if __name__ == '__main__':
    unittest.main()
