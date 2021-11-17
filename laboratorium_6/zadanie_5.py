number = int(input("Podaj liczbę naturalną: "))

def czy(number):
    length = len(str(number))
    for i in range(length - 1):
        if number[i] != number[-(i+1)]:
            return False
    return True

print("Podana cyfra " + ("jest " if(czy(str(number))) else "nie jest ") + "palindromem")
print("Podana postać binarna " + ("jest " if(czy(str(bin(number)[2:]))) else "nie jest ") + "palindromem")