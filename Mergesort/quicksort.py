n = input()
arr = list(map(int, input().split()))


def podziel(arr, start, end):
    pivot = arr[end]
    low = start
    high = end - 1

    while True:
        while low <= high and arr[low] <= pivot:
            low += 1

        while low <= high and arr[high] >= pivot:
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[end], arr[low] = arr[low], arr[end]
    return low


def quicksort(arr, start, end):
    if start < end:
        pivot = podziel(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)
        print(*arr)


quicksort(arr, 0, len(arr) - 1)