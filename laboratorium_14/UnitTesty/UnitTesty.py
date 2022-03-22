from laboratorium_5.zadanie_11 import nwd, nww
from laboratorium_5.zadanie_6 import check_if_prime
from laboratorium_13.zadanie_2 import silnia_rek, silnia_iter
import unittest

#Sprawdzanie NWW liczb
class TestNWWUnit(unittest.TestCase):
    def test_NWW(self):
        self.assertIs(int(nww(120, 60)), 120)
        self.assertIn(int(nww(15, 25)), range(0, 100))

#Sprawdzanie Pierwszości liczby
class TestPrime(unittest.TestCase):
    def test_if_prime(self):
        self.assertEqual(check_if_prime(13), "Pierwsza")
        self.assertNotEqual(check_if_prime(13), "Nie Pierwsza")

#Sprawdzanie silni
class TestSilnia(unittest.TestCase):
    def test_silnia(self):
        self.assertIs(silnia_rek(5), silnia_iter(5))
        self.assertNotEqual(silnia_rek(10), 3628801)

if __name__ == '__main__':
    unittest.main()