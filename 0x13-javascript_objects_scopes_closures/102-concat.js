#!/usr/bin/node

const fs = require('fs');

const files = process.argv.slice(2);

fs.readFile(files[0], 'utf8', (err, content1) => {
  if (err) console.log(err);

  fs.readFile(files[1], 'utf8', (err, content2) => {
    if (err) console.log(err);

    const content = content1 + content2;

    fs.writeFile(files[2], content, 'utf8', (err) => {
      if (err) console.log(err);
    });
  });
});
