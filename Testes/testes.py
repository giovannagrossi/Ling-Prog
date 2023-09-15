#!Essse modulo é so para teste, ele não é pra ser rodado como main!

import unittest
import modulo_teste as ut

# Teste Automatizado X Teste Manual

"""
# Teste exploratório
print(ut.fatorial(5))
print(ut.fatorial(7))
print(ut.fatorial(42))
print(ut.fatorial(8))
"""

# Teste Automatizado Unitáirio

#memorizar isso aqui
class TesteFatorial(unittest.TestCase):
    # Equivalence Partioning Method
    # Equivalence Class Partioning (ECP)
    #testar em partições (categorias)
    def test_greater_than_1(self):
        self.assertEqual(ut.fatorial(2), 2)
        #self.assertEqual(ut.fatorial(3), 6)
        #self.assertEqual(ut.fatorial(4), 24)
        #self.assertEqual(ut.fatorial(5), 120)

    # Boundary Value Analysis ou Boundary Value Test
    #testar nos limites das partições
    def test_equal_1(self):
        self.assertEqual(ut.fatorial(1), 1)
        
    def test_equal_0(self):
        self.assertEqual(ut.fatorial(0), 1)
    
    def test_lesser_than_0(self):
        self.assertEqual(ut.fatorial(-7), 1)
        
    # Data Type Checking
    def test_input_value_type(self):
            self.assertRaises(TypeError, ut.fatorial, "Oi")
    

if __name__ == "__main__":
    unittest.main()







