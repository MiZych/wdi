#INPUT TAKI JAK Z ZADANIA Z PRZECINKAMI!!

def heapify(arr, n, i):
    highest = i
    #Z wykładu wartości dzieci korzenia to indexy: 2k + 1 i 2k + 2
    left = (2*i + 1)
    right = (2*i + 2)

    #Sprawdzenie czy dzieci są mniejsze od rodzica i podmienienie

    if left < n and arr[i] < arr[left]:
        highest = left

    if right < n and arr[highest] < arr[right]:
        highest = right

    #Zamiana zmiennych do wykorzystania w rekurencji, jeśli potomek był większy od rodzica

    if highest != i:
        arr[i], arr[highest] = arr[highest], arr[i]

        #Jesli zaszla zmiana to wywowylujemy jeszcze raz

        heapify(arr, n, highest)

def heapSort(arr):
    n = len(arr)

    #Budujemy MAX-HEAP, zaczynając od ostatniego elementu, wtedy ostatni jakikolwiek rodzic ma index w tablicy równy floor(n/2 - 1)
    #Idziemy od końca więc indexy w tablicy muszą się dekrementować

    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, n , i)

    #Po zakończeniu ustawiana MAX-HEAP ustawiamy pierwszego rodzica na ostatnim węźle drzewa

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = list(map(int, input().split(",")))
heapSort(arr)
n = len(arr)
for i in range(n):
    print("%d" %arr[i], end=",")


#SPRAWDZENIE
# 1,3,1,2,7,9,1,6,1,0,4,2 -> 0,1,1,1,1,2,2,3,4,6,7,9 OK
# 15,3,99,1,25,7,9,9,1,100,6,1,0,12,4,2,9,0,87,122,54 -> 0,0,1,1,1,2,3,4,6,7,9,9,9,12,15,25,54,87,99,100,122 OK
# 0,12,4,2,9,0,87,122,54,1,2,11,55,99 -> 0,0,1,2,2,4,9,11,12,54,55,87,99,122 OK