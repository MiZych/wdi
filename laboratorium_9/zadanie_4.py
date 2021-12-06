import numpy
from copy import deepcopy
#Proszę napisać program rozwiązujący układ równań liniowych o ustalonej liczbie niewiadomych metodą Cramera.
#Liczba niewiadomych powinna być definiowana przez użytkownika.


print("Pamiętaj, że liczba niewiadomych musi być równa liczbie równań!")
number = int(input("Wprowadź ilość równań liniowych: "))
lista_2D = []
afas = "Wprowadź kolejne współczynniki oddzielone spacją przy kolejnych niewiadomych: "
for i in range(number):
    lista_1D = []
    equation = list(map(int, input(afas).split()))
    for j in range(len(equation)):
        lista_1D.append(equation[j])
    lista_2D.append(lista_1D)

# Obliczanie wyznacznika macierzy A

if len(lista_2D[0]) != number:
    print("Wprowadź poprawną liczbę niewiadomych!")
else:
    lista_numpy = numpy.array(lista_2D)
    det_A = round(numpy.linalg.det(lista_numpy), 2)

    if det_A == 0:
        print("Wyznacznik główny równy 0!")
    else:
        # Obliczanie wyznaczników Wi gdzie i ={1,..n} n-liczba niewiadomych
        # Wyznacznik Wi
        frees = list(map(int, input("Wprowadź wyraz wolne do równanań: ").split()))

        def wyznaczniki(x, lista_2D, det_A):
            lista_changes = deepcopy(lista_2D)
            for i in range(len(lista_changes[0])):
                lista_changes[i][x] = frees[i]
            lista_numpy_Wi = numpy.array(lista_changes)
            det_Wi = round(numpy.linalg.det(lista_numpy_Wi), 2)
            resolve = det_Wi / det_A
            return resolve

        # Obliczanie x,y,z itd..
        lista_zmiennych = ["x", "y", "z", "w", "q", "e", "r", "t", "i", "o", "p"]
        for k in range(len(lista_2D[0])):
            print(lista_zmiennych[k], "=", wyznaczniki(k, lista_2D, det_A), end=" ")

#Przypadki testowe: 8x + y +2z = 16
#                   5x - 3y - 7z = -22
#                   0x -5y + 7z = 11
#                   Wynik: x = 1, y =2, z=3






