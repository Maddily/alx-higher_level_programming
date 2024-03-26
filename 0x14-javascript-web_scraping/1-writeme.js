#!/usr/bin/node

const filePath = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

// Write a string to a file.
fs.writeFile(filePath, string, 'utf-8', err => {
  if (err) console.error(err);
});
