#!/usr/bin/node
const argsCount = process.argv.slice(2);
if (argsCount.length === 0) {
  console.log('No argument');
} else {
  console.log(argsCount[0]);
}
