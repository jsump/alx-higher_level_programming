#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2]; // filepath

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // error object if occured
  } else {
    console.log(data); // content of file
  }
});
