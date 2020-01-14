import sys
sys.setrecursionlimit(100000)


def mergeSort(arr):
    print(arr);

    # length of the array
    # find mid point of the array
    mid = int(len(arr)/2)
    # left side of the array. from start till mid
    left = arr[:mid]
    # right side of array from mid to end
    right = arr[mid:]
    # recursion of the left and right array
    mergeSort(left)
    mergeSort(right)
    # note we have three arrays now. main arr left and right

    a=b=c=0

    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            arr[c] = left[a]
            a = a+ 1
        else:
            arr[c] = right[b]
            b = b+1
        k = k+1

    while a < len(left):
        arr[c] = left[a]
        a+=1
        c+=1

    while b < len(right):
        arr[c] = right[b]
        b+=1
        c+=1
    print(arr);


arrayToBeSorted = [23,4,66,7,12,45,60,81,2,3,98];
# print(arrayToBeSorted);

mergeSort(arrayToBeSorted);

# print(arrayToBeSorted);

