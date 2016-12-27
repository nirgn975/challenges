/**
Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

```
flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]
```
**/

var flatten = function (array){
  // TODO: Program me
  let results = [];

  array.forEach(function(value) {
    // Check if it's an array or not.
    if (value instanceof Array) {
      // If it is, takeout it's values.
      value.forEach(function(innerValue) {
        results.push(innerValue);
      });
    } else {
      // if it's isn't, just get back the value.
      results.push(value);
    }
  });

  return results;
}
