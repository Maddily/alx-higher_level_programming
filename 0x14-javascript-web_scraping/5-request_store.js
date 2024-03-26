#!/usr/bin/node

const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

// Get the content of a webpage and write it to a file.
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', err => {
    if (err) console.error(err);
  });
});
