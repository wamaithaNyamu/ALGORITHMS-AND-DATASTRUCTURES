# given an array with x elements, start on the left most element in the array and loof through
# the array until you find the element your searching for in the array

# linear search function

def linearSearch(myArray, searchElement):
    # The array takes in two arguments:
    #     1. myArray - The array being looped over
    #     2.searchElement - The element we will be searching for in the array

    # lengthOfArray -The length of the array
    lengthOfArray = len(myArray);
    for i in range(0, lengthOfArray):
        if myArray[i] == searchElement:
            return i;
    return -1;

#driver code
myArray = [9, 7, 5, 6, 8, 3, 2, 1];
searchElement = 5;
result = linearSearch(myArray, searchElement);
print(result);

if(result == -1):
    print("Element is not in the array");
else:
    print("Element is in the array at index : ", result);

# This algorithm has a time comlexity of O(n)