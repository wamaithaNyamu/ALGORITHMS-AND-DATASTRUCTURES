var x =[];
var y;
function myFunction(x,y){
  for (var i = 0; i < x.length; i++ ){
    console.log(i);
    if (x[i] === y){
      return i;
      }
 
  };
 return -1;

 
};

var myArray = [9, 7, 5, 6, 8, 3, 2, 1];
var searchElement = 5;

var result = myFunction(myArray, searchElement);
console.log(result);
if(searchElement === myArray[result]){
    console.log("The element is in the array at position: ",result);
}else{
    console.log("The element is not in the array")
};