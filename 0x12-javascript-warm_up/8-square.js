#!/usr/bin/node
const argsCount = process.argv.slice(2);
const sizeOfSquare = parseInt(argsCount[0]);

if (!isNaN(sizeOfSquare)) {
  if (sizeOfSquare > 0) {
    for (let i = 0; i < sizeOfSquare; i++) {
      let linesToPrint = '';
      for (let j = 0; j < sizeOfSquare; j++) {
        linesToPrint += 'X';
      }
      console.log(linesToPrint);
    }
  }
} else {
  console.log('Missing size');
}
