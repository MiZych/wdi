import time

n = int(input("Prosze podac liczbe: "))

#Rekurencyjnie
def silnia_rek(n):
    if n > 1:
        return n * silnia_rek(n - 1)
    elif n in (0, 1):
        return 1


#Iteracyjnie
def silnia_iter(n):
    silnia_tmp = 1
    if n in (0, 1):
        return 1
    else:
        for i in range(2, n + 1):
            silnia_tmp = silnia_tmp * i
    return silnia_tmp

if n >= 0:
    start_time = time.time()
    print("Rekurencyjnie", silnia_rek(n))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print("Iteracyjnie", silnia_iter(n))
    print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("Podaj cyfrę większą bądź równą zero")
