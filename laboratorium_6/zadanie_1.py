from math import sqrt
while True:
    print("Program wyznaczający pierwiastki równiania kwadratowego ax^2 + bx + c")
    first = int(input("Podaj wpołczynnik liczby a: "))
    second = int(input("Podaj wpołczynnik liczby b: "))
    third = int(input("Podaj wpołczynnik liczby c: "))

    delta = (second ** 2) - (4*(first * third))

    if first == 0:
        print("Równanie liniowe postaci: ", str(second) + "x", "+", third)
        resolve = ((0 - third) / second)
        print("Rozwiązaniem równania liniowego jest x =", resolve)
    else:
        try:
            x1 = ((-second + sqrt(delta)) / (2 * first))
            x2 = ((-second - sqrt(delta)) / (2 * first))
            if x1 == x2:
                print("Pierwiastakami równania:", str(first) + "x^2", "+", str(second) + "x", "+", third, "to: ", x1)
            else:
                print("Pierwiastakami równania:", str(first) + "x^2", "+", str(second) + "x", "+", third, "to: ", x1,
                      x2)
            raise ValueError()
        except ValueError:
            print("Program nie obsługuje liczb zespolonych")

    what_to_do = input("Co chcesz dalej zrobić? \n T - Kontynuacja programu \n N - Koniec działania programu \n >")
    if what_to_do == "N":
        break

#Przypadki testowe:
#a = 0: 2x -2 wynik to: 1
#delta > 0: 2x^2 + 8x -10 wynnik to: 1 i -5
#delta = 0: x^2 + 6x + 9 wynik to: -3