#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
let wedgeAntillesMovies = 0;

// Print the number of movies where the character Wedge Antilles is present.
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movies = JSON.parse(body).results;

  for (const movie of movies) {
    for (const character of movie.characters) {
      if (character.split('/').includes('18')) {
        wedgeAntillesMovies++;
      }
    }
  }
  console.log(wedgeAntillesMovies);
});
