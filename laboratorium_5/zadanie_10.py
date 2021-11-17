#Program wyznaczający największy wspólny dzielnik 3 zadanych liczb

number_one = int(input("Wprowadź pierszą cyfrę: "))
number_two = int(input("Wprowadź drugą cyfrę: "))
number_third = int(input("Wprowadź trzecią cyfrę: "))

def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)
    return a

nwd2 = nwd(number_one, number_two)
print(nwd(nwd2, number_third))


