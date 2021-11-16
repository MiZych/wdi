summary = int(input("Podaj sumę podciągu: "))
fibonnaci = []

a, b = 0, 1
for i in range(0, 100):
    if a < 1000000:
        fibonnaci.append(a)
        a, b = b, a + b
    else:
        break

for i in range(len(fibonnaci)):
    lista = fibonnaci[0:i]
    if summary == sum(lista):
        print("Istnieje taki podciąg spójny o zadanej sumie:", summary, "taki że:", lista)
