toSort = [8, 1, 5, 15, 3, 20, 11, 7]
print("Tak wygląda tablica: ", toSort)

def mergeSort(tab):
    if len(tab) > 1:
        middle = len(tab) // 2
        left = tab[:middle]
        right = tab[middle:]
        print("Podział na podtablice\nLewa:", left, "\nPrawa: ", right)
        mergeSort(left)
        mergeSort(right)

        temp1 = 0
        temp2 = 0
        temp3 = 0

        while temp1 < len(left) and temp2 < len(right):
            if left[temp1] < right[temp2]:
                tab[temp3] = left[temp1]
                temp1 += 1
            else:
                tab[temp3] = right[temp2]
                temp2 += 1
            temp3 += 1

        while temp1 < len(left):
            tab[temp3] = left[temp1]
            temp1 += 1
            temp3 += 1
        while temp2 < len(right):
            tab[temp3] = right[temp2]
            temp2 += 1
            temp3 += 1
        print("Po: ", tab)

mergeSort(toSort)