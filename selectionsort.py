def selectionSort(arrayToBeSorted):
    for i in range(len(arrayToBeSorted)):
        smallerNumber = i;
        for j in range(i+1, len(arrayToBeSorted)):
            if arrayToBeSorted[smallerNumber] > arrayToBeSorted[j]:
                smallerNumber =j;
        arrayToBeSorted[i], arrayToBeSorted[smallerNumber] = arrayToBeSorted[smallerNumber], arrayToBeSorted[i]

arrayToBeSorted = [23, 4, 1, 7, 45, 99, 22];
print(arrayToBeSorted);

selectionSort(arrayToBeSorted);

print(arrayToBeSorted);