a_zero = 0
a_one = 1
b_one = 2

ciag_a = [0, 1, ]
ciag_b = [2, ]

length_a = len(ciag_a)
length_b = len(ciag_b)

#Obliczenie 20 pierwszych wyrazow ciagu a i 19 b (wiecej nie trzeba bo są za duże)
while length_a > length_b and length_a < 20:
    ciag_b.append(ciag_b[length_a - 2] + (2 * ciag_a[length_a - 2]))
    length_b += 1
    ciag_a.append(ciag_a[length_a - 1] - (ciag_b[length_a - 1] * ciag_a[length_a - 2]))
    length_a += 1

print("Ciąg a", ciag_a)
print("Ciag b", ciag_b)

while True:
    for i in range(len(ciag_a)):
        number = int(input("Podaj kolejną liczbe ciągu a: "))
        if number == ciag_a[i]:
            print("Odpowiadajacy wyraz ciagu b:", ciag_b[i])
            continue
        else:
            break
    break
