#!/usr/bin/node

const obj = require('./101-data').dict;
const newObj = {};

for (const key in obj) {
  const occurrences = obj[key];

  if (!(occurrences in newObj)) {
    newObj[occurrences] = [];
  }

  newObj[occurrences].push(key);
}

console.log(newObj);
