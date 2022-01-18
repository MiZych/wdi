from laboratorium_5.zadanie_6 import check_if_prime
import unittest


#Sprawdzanie Pierwszości liczby
class TestPrime(unittest.TestCase):
    def test_if_prime(self):
        self.assertEqual(check_if_prime(13), "Pierwsza")
        self.assertNotEqual(check_if_prime(13), "Nie Pierwsza")

