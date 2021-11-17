number = int(input("Podaj liczbę naturalną: "))

if number > 0:
    def silnia(number):
        first = 1
        for i in range(2, number + 1):
            first *= i
        return first
    resolve = str(silnia(number))
    for words in range(1, len(resolve) + 1):
        if resolve[-words] != "0":
            print(resolve[-words])
            break
else:
    print("Podaj liczbę naturalną")

