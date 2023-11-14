#!/usr/bin/node
let numOfArg = 0;
exports.logMe = function (item) {
  console.log(numOfArg + ': ' + item);
  numOfArg++;
};
