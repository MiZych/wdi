#Program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

for i in range(1, 1000000):
    suma_first = 0
    for divisors in range(1, int(i/2)+1):
        if i % divisors == 0:
            suma_first += divisors
        for i_second in range(1, suma_first + 1):
            suma_second = 0
            for divisors_second in range(1, int(i_second/2) + 1):
                if i_second % divisors_second == 0:
                    suma_second += divisors_second
            if suma_first == i_second and suma_second == i and i != i_second:
                print("Zaprzyjaznione:", i, i_second)







