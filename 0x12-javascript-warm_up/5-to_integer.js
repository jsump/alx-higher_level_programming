#!/usr/bin/node
const argsCount = process.argv.slice(2);
const firstArgument = argsCount[0];
const intToParse = parseInt(firstArgument);
if (!isNaN(intToParse)) {
  console.log('My number: ' + intToParse);
} else {
  console.log('Not a number');
}
