from statistics import median
first = int(input("Podaj pierwszą liczbę: "))
second = int(input("Podaj drugą liczbę: "))

middle = int(median(range(first, second)))

for i in range(first, second):
    if len(range(first, second)) < 20:
        print(i)

if len(range(first, second)) > 20:
    print(middle - 3, middle - 2, middle - 1, middle + 1, middle + 2, middle + 3)