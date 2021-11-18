#program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy.
number = int(input("Podaj cyfrę: "))

if number > 0:
    divisors_number = []
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors_number.append(i)
    divisors_number.append((number))
    #print(divisors_number)


    length = len(divisors_number)
    if length % 2 == 0:
        if divisors_number[int(length / 2) - 1] * divisors_number[int(length / 2)] == number:
            print(number, "=", divisors_number[int(length / 2) - 1], "*", divisors_number[int(length / 2)])
    else:
        if divisors_number[int(length / 2) - 1] * divisors_number[int(length / 2) + 1] == number:
            print(number, "=", divisors_number[int(length / 2) - 1], "*", divisors_number[int(length / 2) + 1])

else:
    print("Podaj cyfrę naturalną")