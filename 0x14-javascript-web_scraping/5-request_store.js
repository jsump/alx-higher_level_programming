#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // url to request from cmd line
const filePath = process.argv[3]; // filepath to store body response from cmd line arg

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error); // print error if request fails
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err); // print error obj if writing failed
      }
    });
  }
});
