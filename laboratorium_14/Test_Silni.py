from laboratorium_13.zadanie_2 import silnia_rek, silnia_iter
import unittest


#Sprawdzanie silni silni
class TestSilnia(unittest.TestCase):
    def test_silnia(self):
        self.assertIs(silnia_rek(5), silnia_iter(4))
        self.assertNotEqual(silnia_rek(10), 3628800)

