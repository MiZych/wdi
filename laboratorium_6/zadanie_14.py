from math import sqrt
print("Kalkulator liczb zespolonych w postaci wyrażenia algebraicznego: a + bi")
first = int(input("Podaj parametr a: "))
second = int(input("Podaj parametr b: "))
first_second = int(input("Podaj parametr a drugiego wyrażenia: "))
second_second = int(input("Podaj parametr b drugiego wyrażenia: "))
operation = input("Podaj działanie matematyczne: +, -, *, /, **, modul, sprzezenie: ")

if operation == "+":
    print(complex(first, second) + complex(first_second, second_second))
elif operation == "-":
    print(complex(first, second) - complex(first_second, second_second))
elif operation == "*":
    print(complex(first, second) * complex(first_second, second_second))
elif operation == "/":
    print(complex(first, second) / complex(first_second, second_second))
elif operation == "**":
    multiplication = int(input("Do której potegi chcesz podnieść obie liczby?: "))
    print(complex(first, second) ** multiplication)
    print(complex(first_second, second_second) ** multiplication)
#Obliczanie modulu
elif operation == "modul":
    modulo_first = sqrt((first**2) + (second**2))
    modulo_second = sqrt((first_second**2) + (second_second**2))
    print("Moduly liczb zespolonych wynoszą: ", modulo_first, modulo_second)
elif operation == "sprzezenie":
    print(complex(first, -second), complex(first_second, -second_second))



