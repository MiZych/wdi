numbers = list(map(int, input("Podaj 5 cyfr: ").split()))

try:
    if len(numbers) != len(list(dict.fromkeys(numbers))) or len(numbers) > 5 or len(numbers) < 5:
        raise ValueError
    else:
        i = 0
        divs = 0
        while i < 4:
            x = numbers[0 + divs]
            y = numbers[1 + divs]
            if x < y:
                for j in range(1, (y - x)):
                    numbers.insert(1 + divs, y - j)
                divs += (y - x)
                i += 1
            else:
                for j in range(1, (x - y)):
                    numbers.insert(1 + divs, y + j)
                divs += (x - y)
                i += 1
        print(numbers)
except ValueError:
    print("Każda cyfra ma być inna lub podaj dokładnie 5 cyfr po spacji")


#Przypadki testowe
# 0,7,13,8,12 --> [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,10,11,12]
# 1,9,2,8,3 --> [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,3,4,5,6,7,8,7,6,5,4,3]
