# sorting takes on element and sorts it at a time

def insertionSort(x):
    for i in range(1, len(x)):
        # element at the second position - right
        number = x[i];

        # left element at index
        j = i-1;

        # while left most element is greater or equal to zero AND number on the right is less than element on the left
        # boolean AND means both conditions have to be met to execute the while loop
        while j >= 0 and number < x[j]:
             # swap elements
             x[j+1] = x[j]
             j = j-1
        x[j+1] = number



arrayToBeSorted = [23,4,66,7,12,45,60,81,2,3,98];
print(arrayToBeSorted);

insertionSort(arrayToBeSorted)
print(arrayToBeSorted);

