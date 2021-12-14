from copy import deepcopy
#Proszę napisać program rozwiązujący układ równań liniowych o ustalonej liczbie niewiadomych metodą Cramera.
#Liczba niewiadomych powinna być definiowana przez użytkownika.

try:
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

    #Pętla do oblicznia ile elementow jest w sordku list aby sprawdzic czy w kazdej podliscie jest prawdilowa liczba elementow
    suma = 0
    for elementy in lista_2D:
        suma += len(elementy)
    if (suma / number) != number:
        print("Wprowadź poprawną liczbę niewiadomych!")

    else:
        #Obliczanie wyznacznika macierzy A
        print("Lista: ", lista_2D)

        def sariuss(lista_2D):
            first_diagonal = (lista_2D[0][0] * lista_2D[1][1] * lista_2D[2][2]) + (
                        lista_2D[0][1] * lista_2D[1][2] * lista_2D[2][0]) + (
                                         lista_2D[0][2] * lista_2D[1][0] * lista_2D[2][1])
            second_diagonal = (lista_2D[0][2] * lista_2D[1][1] * lista_2D[2][0]) + (
                        lista_2D[0][0] * lista_2D[1][2] * lista_2D[2][1]) + (
                                          lista_2D[0][1] * lista_2D[1][0] * lista_2D[2][2])
            det = first_diagonal - second_diagonal
            return det


        def wyznacznik(lista_2D, number):
            if number == 2:
                det = (lista_2D[0][0] * lista_2D[1][1]) - (lista_2D[0][1] * lista_2D[1][0])
                return det
            elif number == 3:
                det = sariuss(lista_2D)
                return det
            else:
                def removing(werse, column, number, lista_2D):
                    missing = lista_2D[werse][column]
                    lista_removed = deepcopy(lista_2D)
                    for i in range(number):
                        k = 0
                        while k < 1:
                            lista_removed[i].pop(column)
                            k += 1
                    lista_removed.pop(werse)
                    det = wyznacznik(lista_removed, number - 1) * missing
                    if column % 2 != 0:
                        det *= -1
                    return det
                how_many_times = 0
                det_A = 0
                while how_many_times < number:
                    det_A += removing(0, how_many_times, number, lista_2D)
                    how_many_times += 1
                return det_A

        det_A = wyznacznik(lista_2D, number)
        print("det_A", det_A)
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
            suma_changes = 0
            for elements in lista_changes:
                suma_changes += len(elements)
            suma_changes /= 4
            det_Wi = int(wyznacznik(lista_changes, suma_changes))
            resolve = det_Wi / det_A
            return resolve

        # Obliczanie x,y,z itd..
        lista_zmiennych = ["x", "y", "z", "w", "q", "e", "r", "t", "i", "o", "p"]
        for k in range(len(lista_2D[0])):
            print(lista_zmiennych[k], "=", wyznaczniki(k, lista_2D, det_A), end=" ")

except ValueError:
    print("Wprowadź poprawną ilość równań liniowych!")

#Przypadki testowe:
#8x + y +2z = 16
#5x - 3y - 7z = -22
#0x -5y + 7z = 11
#Wynik: x = 1, y = 2, z = 3

#x + y + z = 3
#2x - y - z = 0
#x + 3y + z = 5
#Wynik: x = 1 y = 1 z = 1

#7x + 8y - z + 5w = 40
#6x + 4y + 5z + 3w = 41
#4x - 2y + 5z + 3w = 27
#3x + 5y - 3z + 2w = 12
#Wynik: x = 1 y = 2 z = 3 w = 4





