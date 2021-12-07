#Biblioteka numpy  to biblioteka programistyczna dla języka Python, dodająca obsługę dużych, wielowymiarowych tabel i macierzy.
import numpy
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
#numpy.array(list) konwertuje liste na tablice (list -> array)
#Składnia: numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
#object - obiekt, który chcemy aby był tablicą, dtype - typ danych (jak None to minimalny typ dla sekwencji)
#możemy użyć np. dtype=complex, -copy to po prostu kopiowanie obiektu(domyślnie tak)
#-ndmin-Określa minimalną liczbę wymiarów, jakie powinien mieć wynik.
#Biblioteka numpy działa w oparciu o tablice a nie o listy!
#Tablica różni się od listy m.in: -tablica musi posiadać jeden ten sam typ danych -są stosowane do dłuższych sekwencji znaków
#Musi zawierać wszystkie zagnieżdżone elementy tego samego rozmiaru

        #Obliczanie wyznacznika macierzy A
        print("Lista: ", lista_2D)
        tablica_numpy = numpy.array(lista_2D)
        print("Tablica:", tablica_numpy)
        #numpy.linalg.det(array) - obliczanie wyznacznika tablicy
        det_A = round(numpy.linalg.det(tablica_numpy), 2)

        if det_A == 0:
            print("Wyznacznik główny równy 0!")
        else:
            # Obliczanie wyznaczników Wi gdzie i ={1,..n} n-liczba niewiadomych
            # Wyznacznik Wi
            frees = list(map(int, input("Wprowadź wyraz wolne do równanań: ").split()))

#Funkcja do obliczania wyznacznikow Wi i obliczania i
#deepcopy- Głęboka kopia to proces, w którym proces kopiowania zachodzi rekurencyjnie. Oznacza to najpierw skonstruowanie
#nowego obiektu kolekcji, a następnie rekurencyjne wypełnienie go kopiami obiektów podrzędnych znalezionych w oryginale.
#W przypadku głębokiej kopii kopia obiektu jest kopiowana w innym obiekcie. Oznacza to, że wszelkie zmiany dokonane w kopii
#obiektu nie odzwierciedlają oryginalnego obiektu.

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





