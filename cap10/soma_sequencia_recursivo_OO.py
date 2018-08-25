# -*- coding: utf-8 -*-

#imports
import unittest

#processamento

def somaRecursiva(numero):

    if numero == 0:
        return 0
    else:
        return numero + somaRecursiva(numero - 1)
        
class testeRecursiva(unittest.TestCase):

    def testaSomaRecursiva(self):
        self.assertEqual(0,somaRecursiva(0))
        self.assertEqual(1,somaRecursiva(1))
        self.assertEqual(3,somaRecursiva(2))
        self.assertEqual(6,somaRecursiva(3))
        self.assertEqual(10,somaRecursiva(4))
        self.assertEqual(15,somaRecursiva(5))
        self.assertEqual(21,somaRecursiva(6))
        self.assertNotEqual(2,somaRecursiva(2))

if __name__ == '__main__':
    unittest.main()