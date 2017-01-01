/**
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Implement the method stray which accepts such array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples:

[1, 1, 2] => 2

[17, 17, 3, 17, 17, 17, 17] => 3
**/

function stray(numbers) {
  values = new Map();
  numbers.forEach(function(x){
    values[x] ? values[x] += 1 : values[x] = 1;
  });

  for (let value in values) {
    if (values[value] % 2 != 0){
      return parseInt(value);
    }
  }
  return 0;
}
