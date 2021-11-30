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
    length = len(numbers)
    numbers_sum = []
    div = 0
    for i in range(length):
        numbers_sum.append(numbers[i])
        for j in range(1, length - div):
            numbers_sum.append(numbers[i] + numbers[j + div])
        div += 1
    v = 1
    for i in range(length):
        numbers_sum.append(numbers[i])
        for k in range(v, length):
            numbers_sum.append(sum(numbers[i:(k + 1)]))
        v += 1
    numbers_sum = list(set(numbers_sum))
    numbers_sum.sort()
    for primes in prime_numbers:
        for k in range(len(numbers_sum)):
            if numbers_sum[k] % primes == 0:
                print("(", primes, numbers_sum[k], ")", end="")
                break
sum_prime(prime_numbers, numbers)

#Przypadki testowe
#sum_prime(prime_numbers, [7,13,18,23,24]) --> "(2 18)(3 18)(5 20)(7 7)(13 13)(17 85)(19 38)(23 23)(31 31)(37 37)(41 41)(47 47)(61 61)"
#sum_prime(prime_numbers, [3,5,7,9,11,13]) --> "(2 8)(3 3)(5 5)(7 7)(11 11)(13 13)"
