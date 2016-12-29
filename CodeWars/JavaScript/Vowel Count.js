/**
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.
**/

function getCount(str) {
  var vowels = ['a', 'e', 'i', 'o', 'u'];
  var vowelsCount = 0;

  for (variable in str) {
    if (vowels.indexOf(str[variable].toLowerCase()) > -1) {
      vowelsCount++;
    }
  }

  return vowelsCount;
}
