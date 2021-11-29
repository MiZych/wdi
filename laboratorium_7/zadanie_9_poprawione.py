numbers = list(map(int, input("Podaj 5 cyfr: ").split()))

try:
    if len(numbers) != len(list(dict.fromkeys(numbers))) or len(numbers) > 5 or len(numbers) < 5:
        raise ValueError
    else:
        i = 0
        how_much = 0
        divs = 0
        while i < 4:
            x = numbers[0 + how_much]
            y = numbers[1 + how_much]
            if x < y:
                for j in range(1, (y - x)):
                    numbers.insert(1 + divs, y - j)
                    how_much += 1
                how_much += 1
                divs += (y - x)
                i += 1
            else:
                for j in range(1, (x - y)):
                    numbers.insert(1 + divs, y + j)
                    how_much += 1
                how_much += 1
                divs += (x - y)
                i += 1
        print(numbers)
except ValueError:
    print("Każda cyfra ma być inna lub podaj dokładnie 5 cyfr po spacji")



