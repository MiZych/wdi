#Plansze
from random import randint
height = int(input("Wprowadź wysokość: "))
width = int(input("Wprowadź szerokość: "))


def making_list(height):
    #1 - first_line, 2 - width_line
    how_many = []
    how_many.append(1)
    for i in range(1, height * 3):
        if i % 2 == 0 and i % 3 == 0:
            how_many.append(1)
        else:
            if i % 2 == 0:
                how_many.append(2)
            elif i % 3 == 0:
                how_many.append(1)
    how_many.append(1)
    return how_many

list_of_lines = making_list(height)


def redirect(list_of_lines, width):
    start = "|"
    middle = "-"
    first_line = start + (((middle * 3) + start) * (width - 1)) + (middle * 3) + start
    width_line = start + (((" " * 3) + start) * (width - 1)) + (" " * 3) + start
    with open("output.txt", "a") as f:
        for i in range(len(list_of_lines)):
            if list_of_lines[i] == 1:
                print(first_line, file=f)
            elif list_of_lines[i] == 2:
                print(width_line, file=f)

redirect(list_of_lines, width)