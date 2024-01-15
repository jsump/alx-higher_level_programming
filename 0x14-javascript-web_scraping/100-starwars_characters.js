#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // get movie ID from cmd line arg
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // print error if request fails
  } else {
    const movie = JSON.parse(body);
    movie.characters.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError); // print error if request fails
        } else {
          const char = JSON.parse(charBody);
          console.log(char.name); // ptint character name
        }
      });
    });
  }
});
