#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // get movieId from cmd line
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
// construct movie API

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // print error if request fails
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title); // print movie title
  }
});
