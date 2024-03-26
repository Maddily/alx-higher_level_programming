#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

// Display the status code of a GET request.
request(url, (error, response, body) => {
  if (error) console.error(error);
  console.log(response.statusCode);
});
