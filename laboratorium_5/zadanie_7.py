number = int(input("Podaj cyfrę: "))
divisors_list = []
for i in range((int(number/2)) + 1):
    if i == 0:
        divisors_list.append(i)
    elif number % i == 0:
        divisors_list.append(i)
divisors_list.append(number)
print("Podzielniki liczby", number, "to:", divisors_list)




