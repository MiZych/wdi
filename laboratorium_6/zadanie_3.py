number = int(input("Podaj cyfrę naturalną: "))

fibonnaci = []

a, b = 0, 1
for i in range(0, 100):
    if a < 100000000:
        fibonnaci.append(a)
        a, b = b, a + b
    else:
        break


fibonnaci_power =[]
for i in range(len(fibonnaci)):
    div = 1
    while div < len(fibonnaci):
        fibonnaci_power.append(fibonnaci[i] * fibonnaci[div])
        if number == (fibonnaci[i] * fibonnaci[div]):
            print("Istnieje taki iloczyn dwóch dowolnych liczb ciągu Fibonnaciego: ", fibonnaci[i], fibonnaci[div])
        div += 1
#Do sprawdzania
print(set(fibonnaci_power))
