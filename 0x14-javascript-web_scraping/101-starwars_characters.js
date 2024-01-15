#!/usr/bin/node
const request = require('request');

// this will retrive charName from characterUrl
const getCharName = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error); // Reject promise if error occurs
      } else {
        const character = JSON.parse(body);
        resolve(character.name); // Resolve promise with charName
      }
    });
  });
};

// This retrives and displays the char of Staw Wars
const movieChars = async (movieId) => {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request.get(apiUrl, (error, response, body) => {
        if (error) {
          reject(error); // Reject promise if there's an error
        } else {
          resolve(JSON.parse(body)); // resolve with film response
        }
      });
    });
    for (const characterUrl of filmResponse.characters) {
      const charName = await getCharName(characterUrl); // Retrive the charName
      console.log(charName); // Print charNAme
    }
  } catch (error) {
    console.error(error); // Print error if it occurs
  }
};

const movieId = process.argv[2]; // get MovieId from cmd line arg
movieChars(movieId); // Fuvntion to retrieve and siplay chars
