#!/usr/bin/node

const integers = process.argv.slice(2).map((e) => parseInt(e));

if (integers.length < 2) {
  console.log(0);
} else {
  const largest = Math.max(...integers);
  const withoutLargest = integers.filter((e) => e !== largest);

  console.log(Math.max(...withoutLargest));
}
