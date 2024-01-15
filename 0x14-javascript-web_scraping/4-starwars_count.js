#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2]; // get api from cmd line arg
const charId = '18'; // wedge antilles character ID

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print error if request fails
  } else {
    const films = JSON.parse(body).results;
    const moviesWithCharID = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/films/${charId}/`));
    console.log(moviesWithCharID.length); // Print number of movies with Wedge Antilles
  }
});
