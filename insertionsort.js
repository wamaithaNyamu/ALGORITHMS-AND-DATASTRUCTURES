var x;
function insertionSort( x){
  for(var i =1; i< x.length; i++){
    number = x[i];
    j = i-1;

    while (j>=0 && number < x[j]){
      x[j+1] = x[j];
      j = j-1;
    }
    x[j+1] = number;

  }
}
arrayToBeSorted = [23,4,66,7,12,45,60,81,2,3,98];
console.log(arrayToBeSorted);

insertionSort(arrayToBeSorted);
console.log(arrayToBeSorted);

