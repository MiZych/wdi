number = int(input("Podaj cyfrę: "))
how_many = int(input("W jakim zakresie ciągu Fibonnaciego chcesz sprawdzić: "))
fibonacci = []
fib1 = 0
fib2 = 1
for i in range(how_many + 1):
    if i == 0:
        fibonacci.append(i)
    else:
        fib1, fib2 = fib2, fib1 + fib2
        fibonacci.append(fib1)

for i in range(how_many):
    if number == fibonacci[i] * fibonacci[i+1]:
        print("Jest iloczynem dwóch kolejnych liczb ciągu Fibonnaciego: ", fibonacci[i], fibonacci[i+1])
    else:
        continue



