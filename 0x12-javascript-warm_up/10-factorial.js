#!/usr/bin/node
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
};
const argsCount = process.argv.slice(2);
const input = parseInt(argsCount[0]);
console.log(factorial(input));
