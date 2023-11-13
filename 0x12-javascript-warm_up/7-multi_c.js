#!/usr/bin/node
const argsCount = process.argv.slice(2);
const firstArgument = argsCount[0];
const intToParse = parseInt(firstArgument);

if (!isNaN(intToParse)) {
  for (let i = 0; i < intToParse; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
