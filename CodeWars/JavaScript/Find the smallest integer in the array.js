/**
Find the smallest integer in the array.

Given an array of integers your solution should find the smallest integer. For example:
* Given [34, 15, 88, 2] your solution will return 2
* Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.
**/

class SmallestIntegerFinder {
  findSmallestInt(args) {
    let smallestValue = args[0];
    for (let value of args) {
      if (value < smallestValue) {
        smallestValue = value;
      }
    }
    return smallestValue;
  }
}

/** ---------- **/

class SmallestIntegerFinder {
  findSmallestInt(args) {
    return Math.min(...args);
  }
}
