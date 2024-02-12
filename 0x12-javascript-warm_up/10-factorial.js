#!/usr/bin/node

const number = parseInt(process.argv[2]);

function findFactorial (number) {
  if (isNaN(number)) {
    return 1;
  } else if (number === 1) {
    return 1;
  } else {
    return number * findFactorial(number - 1);
  }
}

console.log(findFactorial(number));
