import math
numbers = list(map(int, input("Podaj cyfry: ").split()))

prime_numbers = []

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def generator_primes(n):
    for i in range(2, n+1):
        if is_prime(i):
            prime_numbers.append(i)

generator_primes(sum(numbers))

def sum_prime(prime_numbers, numbers):
    res = ""
    for primes in prime_numbers:
        suma = 0
        for number in numbers:
            if number % primes == 0:
                suma += number
        if suma > 0:
            res += "(" + str(primes) + " " + str(suma) + ")"
    print(res)
sum_prime(prime_numbers, numbers)

#Przypadki testowe
#sum_prime(prime_numbers, [7,13,18,23,24]) --> "(2 42)(3 42)(7 7)(13 13)(23 23)"
#sum_prime(prime_numbers, [3,5,7,9,11,13]) --> "(3 12)(5 5)(7 7)(11 11)(13 13)"

