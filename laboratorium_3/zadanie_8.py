height = int(input("Podaj wysokość choinki: "))

i = 1
space = " "
spaces = height - 2
number_of_stars = 3
trunk = "U"
top = "X"
star = "*"

print((space * height) + top)
while height - 1 >= i:
    print((space * spaces), "*" * number_of_stars)
    i += 1
    spaces -= 1
    number_of_stars += 2
print((space * height) + trunk)