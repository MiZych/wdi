#Program sprawdzający czydana liczb jest liczbą pierwszą
from math import sqrt
number = int(input("Podaj cyfrę: "))

yes = "Pierwsza"
no = "Nie pierwsza"
def check(number):
    if number == 2:
        print(yes)
    elif number % 2 == 0 or number <= 1:
        print(no)
    else:
        for dzielnik in range(3, int(sqrt(number)) + 1):
            if number % dzielnik == 0:
                return no
        return yes

print(check(number))