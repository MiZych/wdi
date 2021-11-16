fibonnaci = []

a, b = 0, 1
for i in range(0, 100):
    if a < 1000000:
        fibonnaci.append(a)
        a, b = b, a + b
    else:
        break

print(fibonnaci)