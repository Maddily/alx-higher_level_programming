#!/usr/bin/node

const filePath = process.argv[2];
const fs = require('fs');

// Read and print data from a file.
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
