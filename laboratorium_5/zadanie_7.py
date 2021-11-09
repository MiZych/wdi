number = int(input("Podaj cyfrę: "))
divisors_list = []

if number == 0:
    print("Podzielnikami liczby 0 są wszystkie liczby rzeczywiste z wyłączeniem 0")
else:
    original = number
    number = abs(number)
    for i in range((int(number / 2)) + 1):
        if i == 0:
            pass
        elif number % i == 0:
            divisors_list.append(-i)
            divisors_list.append(i)
    divisors_list.append(number)
    divisors_list.append(-number)
    print("Podzielniki liczby", original, "to:", divisors_list)
