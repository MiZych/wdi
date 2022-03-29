import os

def quickSort(arr):
    left = []
    equal = []
    right = []
    pivot = arr[0]

    for elements in arr:
        if elements < pivot:
            left.append(elements)
        elif elements == pivot:
            equal.append(elements)
        elif elements > pivot:
            right.append(elements)

    resolve = left + equal + right
    return resolve


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()