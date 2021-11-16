from math import sqrt
number = int(input("Podaj liczbę którą chcesz spierwiastkować: "))

#number^2 = a => number^2 - a = 0
x_one = number - 1
x_two = x_one - (((x_one ** 2) - number) / (2*x_one))
x_three = x_two - (((x_two ** 2) - number) / (2*x_two))
print("Wynik z metody Newtona:", x_three)
print("Wynik z kalkulatora:", sqrt(number))