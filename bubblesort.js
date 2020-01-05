function bubbleSort(arr){
  n =arr.length
  for(var i =0; i < n; i++){
    for(var j = 0; j < n-i-1; j++){
      if(arr[j] > arr[j+1]){
        var tempVar = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tempVar;
      }
    }
  }
}
arr = [79,5,4,76,23,4,55,78,10001];
console.log(arr)
bubbleSort(arr);
console.log(arr)
