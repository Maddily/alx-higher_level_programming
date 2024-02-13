#!/usr/bin/node

let alreadyPrinted = 0;

exports.logMe = function (item) {
  console.log(`${alreadyPrinted}: ${item}`);
  alreadyPrinted++;
};
