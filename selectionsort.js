var arrayToBeSorted ;
function selectionSort(arrayToBeSorted){

  for(var i =0; i < arrayToBeSorted.length; i++){
    for(var j =i+ 1; j < arrayToBeSorted.length; j++){
      if(arrayToBeSorted[i] > arrayToBeSorted[j]){
         var tempArray = arrayToBeSorted[i];;
         arrayToBeSorted[i] = arrayToBeSorted[j];
       arrayToBeSorted[j] = tempArray;
     }

    }

  }
  return arrayToBeSorted;


}
arrayToBeSorted = [23, 4, 50, 7, 45, 99, 22];
console.log(arrayToBeSorted);
selectionSort(arrayToBeSorted);
console.log(arrayToBeSorted);
