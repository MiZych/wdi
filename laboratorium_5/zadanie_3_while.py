from math import sqrt
number = int(input("Podaj liczbę którą chcesz spierwiastkować: "))

#number^3 = a => number^3 - a = 0

i = 0
x_one = number - 1
while i < 10:
    x_two = 0.5 * (x_one + (number / x_one))
    x_one = x_two
    i += 1
    if i == 9:
        print(x_one)