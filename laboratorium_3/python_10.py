from random import randint

while True:
    first = int(input("Proszę podać 1 cyfrę: "))
    second = int(input("Proszę podać 2 cyfrę: "))
    operation = input("Podaj operację matematyczną (+, -, *, /, **, ^, x): ")

    def operations():
        if operation == "+":
            summary = first + second
            print("Suma: ", summary)
        elif operation == "-":
            subtraction = first - second
            print("Różnica: ", subtraction)
        elif operation == "*":
            multiplication = first * second
            print("Iloczyn: ", multiplication)
        elif operation == "/":
            division = first / second
            print("Iloraz: ", division)
        elif operation == "**":
            power = first ** second
            print("Potęga: ", power)
        elif operation == "^":
            sqrt_f = first ** (1/2)
            sqrt_s = second ** (1/2)
            print("Pierwiastkowanie dwóch liczb: ", sqrt_f, sqrt_s)

    if operation == "x":
        range_p = int(input("Podaj początkowy zakres, z którego zostanie wybrana liczba: "))
        range_k = int(input("Podaj końcowy zakres, z którego zostanie wybrana liczba: "))
        first = randint(range_p, range_k)
        second = randint(range_p, range_k)
        operation = input("Podaj operację matematyczną (+, -, *, /, **, ^): ")
        operations()
    else:
        operations()

    check = input("Czy chcesz wprowadzić nowe dane? \nT - Wprowadź nowe dane \nN - Zakończ \n>")
    if check == "N":
        break

