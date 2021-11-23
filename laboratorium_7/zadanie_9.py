numbers = list(map(int, input("Podaj 5 cyfr: ").split()))
numbers.sort()
try:
    if len(numbers) != len(list(dict.fromkeys(numbers))) or len(numbers) > 5 or len(numbers) < 5:
        raise ValueError
    else:
        lower = numbers[0]
        upper = numbers[-1]
        resolve = list(range(lower, upper + 1))
        print(resolve)
except ValueError:
    print("Każda cyfra ma być inna lub podaj dokładnie 5 cyfr po spacji")



