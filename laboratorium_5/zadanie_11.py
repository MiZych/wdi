#Program wyznaczający NWW 3 zadanych liczb


def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)
    return a

#NWW(a,b) = a*b / NWD(a,b)
def nww(a, b):
    return ((a*b) / nwd(a,b))


if __name__ == '__main__':
    number_one = int(input("Wprowadź pierszą cyfrę: "))
    number_two = int(input("Wprowadź drugą cyfrę: "))
    number_third = int(input("Wprowadź trzecią cyfrę: "))

    nwd2 = nwd(number_one, number_two)
    nwd3 = nwd(nwd2, number_third)
    nww2 = nww(number_one, number_two)
    nww3 = nww(nww2, number_third)

    print(nww3)