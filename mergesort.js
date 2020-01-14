function mergeSort(x){
  mid = x.length/2
  left = x.slice(0,mid)
  console.log(left)
  right = x.slice(mid)
  console.log(right)

  var a,b,c;
  a=b=c=0;

  while(a < left.length && b < right.length){
    if(left[a] < right[b]){
      x[c] = left[a];
      a++;
    }
    else{
      x[c] = right[b];
      b++;
    }
  c++
  }

  while (a < left.length){
    x[c] = left[a];
    a++;
    c++;
  }
  while (b < right.length){
    x[c] = right[b];
    b++;
    c++;
  }


}
var x = [23,4,66,7,67,12,45,60,81,2,3,98];
console.log(x)
mergeSort(x)
console.log(x)