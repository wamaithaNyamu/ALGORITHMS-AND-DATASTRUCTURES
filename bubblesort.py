def bubbleSort(arrayToBeSorted):
    arrayLength = len(arrayToBeSorted);
    for i in range(arrayLength):
        for j in range(0, arrayLength-i-1):
            if arrayToBeSorted[j]> arrayToBeSorted[j+1]:
                # swap
                arrayToBeSorted[j], arrayToBeSorted[j+1]= arrayToBeSorted[j+1], arrayToBeSorted[j];


arr = [79,5,4,76,23,4,55,78,10001];
print(arr)

bubbleSort(arr)

print(arr)