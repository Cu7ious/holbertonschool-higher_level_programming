#!/usr/bin/node
/**
 * This script prints the addition of 2 integers
 *
 * The first argument is the first integer
 * The second argument is the second integer
 * @NB: You have to define a function with this prototype: function add(a, b)
 * @NB: You must use console.log(...) to print all output
 * @NB: You are not allowed to use var
 */

/**
 * add - adds its arguments
 * @a: first summand, int
 * @b: second summand, int
 *
 * Return: sum a + b or Infinity.
 * If type of one of the arguments is wrong: NaN
 */
function add (a, b) {
  return Number(a) + Number(b);
}

console.log(add(process.argv[2], process.argv[3]));
