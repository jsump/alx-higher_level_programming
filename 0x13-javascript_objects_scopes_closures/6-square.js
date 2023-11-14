#!/usr/bin/node
const SquareFrom = require('./5-square');
class Square extends SquareFrom {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let squareString = '';
    for (let i = 0; i < this.height; i++) {
      squareString += c.repeat(this.width) + '\n';
    }
    console.log(squareString);
  }
}
module.exports = Square;
