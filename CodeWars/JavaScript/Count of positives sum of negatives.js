/**
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array:

* C#/Java: new int[] {} / new int[0];
* C++: std::vector<int>();
* JavaScript/CoffeeScript/PHP/Haskell: [];

ATTENTION!
The passed array should NOT be changed. Read more here.

For example:
```haskell
**/

function countPositivesSumNegatives(input) {
  let sum = [0, 0];

  if (!input || !input.length) {
    return [];
  }

  for (let num of input) {
    if (num > 0) {
      sum[0] += 1;
    } else {
      sum[1] += num;
    }
  }

  return sum;
}
