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

  // Create an array of promises to fetch character names.
  const promises = characters.map(character => {
    return new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  // Wait for all promises to resolve before printing the names.
  Promise.all(promises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.log(error);
    });
});
