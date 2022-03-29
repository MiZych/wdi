# Insertion sort in Python
def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key > arr[j]:
    # For ascending order, change key> arr[j] to key < arr[j].
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key

arr = [15, 50, -27, -4, 10 ]
insertion_sort(arr)
print('Sorted Array in descending Order:')
print(arr)