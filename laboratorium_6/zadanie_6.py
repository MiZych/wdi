zasieg = int(input("Podaj zakres końcowy: "))

if zasieg > 0:
    print("Liczba 1 jest dwu-trzy-piątkowa")
    for i in range(1, zasieg + 1):
        if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 2 == 0 and i % 3 == 0) or (i % 2 == 0 and i % 5 == 0) or (i % 3 == 0 and i % 5 == 0) or (i % 2 == 0 and i % 3 == 0 and i % 5 == 0):
            print("Liczba", i, "jest dwu-trzy-piątkowa")
else:
    print("Podaj liczbę naturalną")