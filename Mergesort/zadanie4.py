def quicksort(arr):
    if len(arr) < 2:
        return arr
    left = []
    merge = []
    right = []
    for elements in arr:
        if elements < arr[0]:
            left.append(elements)
        elif elements > arr[0]:
            right.append(elements)
        else:
            merge.append(elements)
    resolve = quicksort(left) + merge + quicksort(right)
    print(*resolve)
    return(resolve)

n = input().strip().split()
arr = [int(x) for x in input().strip().split()]
quicksort(arr)

