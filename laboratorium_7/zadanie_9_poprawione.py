numbers = list(map(int, input("Podaj 5 cyfr: ").split()))
try:
    if len(numbers) != len(list(dict.fromkeys(numbers))) or len(numbers) > 5 or len(numbers) < 5:
        raise ValueError
    else:
        lower = numbers[0]
        upper = numbers[1]
        if lower < upper:
            for i in range(lower + 1, upper):
                numbers.insert(1, i)
        else:
            for i in range(1, lower - upper):
                numbers.insert(1, upper + i)
    print(numbers)
except ValueError:
    print("Każda cyfra ma być inna lub podaj dokładnie 5 cyfr po spacji")



