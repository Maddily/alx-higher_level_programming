#!/usr/bin/node

const episode = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

// Display the title of a Star Wars movie where the episode number matches a given integer.
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});
