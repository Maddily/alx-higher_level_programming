#!/usr/bin/node

const episodeId = process.argv[2];
const request = require('request');
const filmsUrl = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

// Display all characters of a Star Wars movie.
request(filmsUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const name = JSON.parse(body).name;
      console.log(name);
    });
  }
});
