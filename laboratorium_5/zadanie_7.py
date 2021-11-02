number = int(input("Podaj cyfrę: "))
divisors_list = []
for i in range(number + 1):
    if i == 0:
        divisors_list.append(i)
    elif number % i == 0:
        divisors_list.append(i)

print("Podzielniki liczby", number, "to:", divisors_list)




