#Program wyszukujący liczby doskonałe mniejsze od miliona.

for i in range(1, 1000000):
    divisors_list = []
    for dzielniki in range(1, int((i/2) + 1)):
        if i % dzielniki == 0:
            divisors_list.append(dzielniki)
    if sum(divisors_list) == i:
        print(i)
