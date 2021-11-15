print("Kalkulator liczb zespolonych w postaci wyrażenia algebraicznego: a + bi")
first = int(input("Podaj parametr a: "))
second = int(input("Podaj parametr b: "))
first_second = int(input("Podaj parametr a drugiego wyrażenia: "))
second_second = int(input("Podaj parametr b drugiego wyrażenia: "))
operation = input("Podaj działanie matematyczne: +, -, *, /, **: ")

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
