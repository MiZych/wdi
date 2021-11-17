number = int(input("Podaj cyfrę naturalną: "))
zasieg = int(input("Wprowadź liczbę rozpatrywanych wyrazów ciągu: "))

if number > 0:
    for i in range(2, zasieg + 1):
        operation = (i ** 2) + i + 1
        if number % operation == 0:
            print("Jest wielokrotnoscią wyrazu ")
            break
        else:
            print("Nie jest")
            break
else:
    print("Podaj liczbę naturalną")
