from laboratorium_5.zadanie_11 import nwd, nww
import unittest
import pytest


class TestNWWUnit(unittest.TestCase):
    def test_NWW(self):
        self.assertIs(int(nww(120, 60)), 120)
        self.assertIn(int(nww(15, 25)), range(0, 100))

def test_NWW_PyTest():
    assert 120 == nww(120, 60)
    assert 60 == nww(15, 25)

