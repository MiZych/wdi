import decimal
from decimal import *
first = int(input("Podaj licznik: "))
second = int(input("Podaj mianownik: "))
third = int(input("Podaj do ilu miejsc po przecinku: "))

getcontext().prec = third
if first > 0 and second > 0 and third > 0:
    operation = decimal.Decimal(first) / decimal.Decimal(second)
    print(operation)
else:
    print("Wczytaj liczby naturalne")