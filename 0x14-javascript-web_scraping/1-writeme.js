#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2]; // filepath from cmd line arg
const content = process.argv[3]; // retrieve string to write from cmd line arg

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // print error of obj if occured
  } else {
    console.log('success'); // sucess message
  }
});
