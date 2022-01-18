from laboratorium_5.zadanie_11 import nwd, nww
from laboratorium_5.zadanie_6 import check_if_prime
from laboratorium_13.zadanie_2 import silnia_rek, silnia_iter
import pytest



def test_nww():
    assert 120 == nww(120, 60)
    assert 75 == nww(15, 25)

def test_prime():
    assert "Pierwsza" == check_if_prime(13)
    assert "Nie pierwsza" == check_if_prime(15)

def test_silnia():
    assert silnia_rek(5) == silnia_iter(5)
    assert silnia_rek(7) == silnia_iter(6)
