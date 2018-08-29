#!/usr/bin/node
/**
 * This script prints x times "C is fun"
 *
 * Where x is the first argument of the script
 * When can’t be converted to an integer: "Missing number of occurrences"
 * @NB: You can use only two console.log
 * @NB: You must use a loop (while, for, etc.)
 */
let x = !isNaN(Number(process.argv[2])) ? Number(process.argv[2]) : null;

if (!x) {
  console.log('Missing number of occurrences');
  process.exit();
}

for (let i = 0; i < x; ++i) {
  console.log('C is fun');
}
