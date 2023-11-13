#!/usr/bin/node
const addition = (a, b) => {
  return a + b;
};
const argsCount = process.argv.slice(2);
const firstInteger = parseInt(argsCount[0]);
const secondInteger = parseInt(argsCount[1]);

if (!isNaN(firstInteger) && !isNaN(secondInteger)) {
  console.log(addition(firstInteger, secondInteger));
} else {
  console.log('NaN');
}
