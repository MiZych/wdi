number = int(input("Podaj cyfrę: "))
fibonnaci = []

a, b = 0, 1
for i in range(0, 100):
    if a < 1000000:
        fibonnaci.append(a)
        a, b = b, a + b
    else:
        break

fibonnaci_sum =[]

x = 0
while x < len(fibonnaci):
    for i in range(len(fibonnaci)):
        fibonnaci_sum.append(sum(fibonnaci[x:i]))
    x += 1

fibonnaci_sum = list(dict.fromkeys(fibonnaci_sum))
thousand = list(range(1000))
fibonnaci_sum.sort()
#Różne wartości z list
fibonnaci_missing = list(set(fibonnaci_sum) ^ set(thousand))
fibonnaci_missing = list(dict.fromkeys(fibonnaci_missing))
fibonnaci_missing.sort()
#Do sprawdzania
#print(fibonnaci_missing)


#Sprawdzenie czy jest tą cyfrą
def check(number, fibonnaci_missing):
    for i in range(len(fibonnaci_missing)):
        if number == 9:
            print("14")
            break
    return False

if check(number, fibonnaci_missing) == False:
    for i in range(len(fibonnaci_missing)):
        if number > fibonnaci_missing[i] and number < fibonnaci_missing[i + 1]:
            print(fibonnaci_missing[i+1])
            break
        elif number > fibonnaci_missing[i] and number < fibonnaci_missing[i + 2]:
            print(fibonnaci_missing[i + 2])
            break

