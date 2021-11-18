number = int(input("Wprowadź liczbę naturalną: "))

if number > 0:
    system = int(input("W jakim systemie chcesz zamienić liczbę: 2, 8, 10, 16: "))

    if system == 2: print(bin(number)[2:])
    elif system == 8: print(oct(number)[2:])
    elif system == 10: print(number)
    elif system == 16: print(hex(number)[2:])
    else: print("Wybierz poprawny system")
else:
    print("Wprowadź liczbę naturalną")