#!/usr/bin/node
/**
 * This script prints a square
 *
 * The first argument is the size of the square
 * When first argument can’t be converted to an integer: prints "Missing size"
 * @NB: You must use the character X to print the square
 * @NB: You must use console.log(...) to print all output
 * @NB: You are not allowed to use var
 * @NB: You must use a loop (while, for, etc.)
 */
let n = !isNaN(Number(process.argv[2])) ? Number(process.argv[2]) : null;

if (!n) {
  console.log('Missing size');
  process.exit();
}

const range = [...Array(n)];
const x = range.map(() => 'X').join('');

while (n !== 0) {
  console.log(x);
  --n;
}
