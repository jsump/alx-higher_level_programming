#!/usr/bin/node
const argsCount = process.argv.slice(2);
const integers = argsCount.map(arg => parseInt(arg));
if (integers.length < 2) {
  console.log(0);
} else {
  integers.sort((a, b) => b - a);
  console.log(integers[1]);
}
