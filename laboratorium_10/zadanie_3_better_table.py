#Plansze
import sys

height = int(input("Wprowadź wysokość: "))
width = int(input("Wprowadź szerokość: "))

def create_board(height, width):
    start = "╔"
    middle = "═"
    separator = "╤"
    end = "╗"
    to_width = "║"
    solo_width = "│"
    separator_width = "╟"
    opposite_sepatartor_width = "╢"
    middle_width = "─"
    ending_separator = "╧"
    first_line = start + (((middle * 3) + separator) * (width - 1)) + (middle * 3) + end
    width_line = to_width + (((" " * 3) + solo_width) * (width - 1)) + (" " * 3) + to_width
    separating_line = separator_width + (((middle_width * 3) + solo_width) * (width - 1)) + (middle_width * 3) + opposite_sepatartor_width
    ending_line = "╚" + (((middle * 3) + ending_separator) * (width - 1)) + (middle * 3) + "╝"
    print(first_line)
    for i in range(1, height * 3):
        if i % 2 == 0 and i % 3 == 0:
            print(separating_line)
        else:
            if i % 2 == 0:
                print(width_line)
            elif i % 3 == 0:
                print(separating_line)
    print(ending_line)

create_board(height, width)