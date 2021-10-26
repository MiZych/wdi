first = int(input("Podaj pierwszą liczbę: "))
second = int(input("Podaj drugą liczbę: "))

def function_multiplication():
    print("Wynik dodawania:", first + second)
    print("Wynik odejmowania: ", first - second)
    print("Wynik dzielenia: ", first / second)
    print("Wynik potęgowania 1 liczby do drugiej:", first ^ second)
    print("Wyniki pierwiastków 2 stopnia liczb 1 i 2:", first ** (1/2), second ** (1/2))

def function_print():
    if first * second == 10:
        function_multiplication()
        print("Wynik mnożenia: ", first * second, "Yay!")
    else:
        function_multiplication()
        print("Wynik mnożenia:", first * second)


if (first < 0) and (second < 0):
    print("Obydwie liczby są mniejsze od zera")
    pass
elif (first > 0) and (second < 0):
    second = second * (-1)
    function_print()
elif (first < 0) and (second > 0):
    first = first * (-1)
    function_print()
else:
    function_print()


