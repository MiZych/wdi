import math

n = int(input("Podaj zakres końcowy N: "))
if n > 0:
    print("Program znajdujacy liczby pierwsze z przedzialu <2,n>.")
    liczby = [True] * (n + 1)  # tworzymy n+1 elementowa tablice
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if liczby[i]:  # jezeli liczba jest pierwsza
            for k in range(i * i, n + 1, i):  # oznacz wszystkie jej wielokrotnosci jako liczby zlozone
                liczby[k] = False
    print("Liczby pierwsze z przedzialu <2," + str(n) + "> : ")
    for i in range(2, n + 1):  # wypisujemy elementy utworzonej tablicy
        if liczby[i]:
            print(str(i), end=" | ")


else:
    print("Podaj liczbę naturalną")