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
        if delta < 0:
            try:
                sqrt_delta = sqrt(delta)
            except ValueError:
                print("Program nie obsługuje liczb zespolonych")
        else:
            sqrt_delta = sqrt(delta)
            x1 = ((-second + sqrt_delta) / 2 * first)
            x2 = ((-second - sqrt_delta) / 2 * first)
            if x1 == x2:
                print("Pierwiastakami równania:", str(first) + "x^2", "+", str(second) + "x", "+", third, "to: ", x1)
            else:
                print("Pierwiastakami równania:", str(first) + "x^2", "+", str(second) + "x", "+", third, "to: ", x1, x2)
    what_to_do = input("Co chcesz dalej zrobić? \n T - Kontynuacja programu \n N - Koniec działania programu \n >")
    if what_to_do == "N":
        break
