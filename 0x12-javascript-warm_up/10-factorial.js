#!/usr/bin/node
/**
 * This script computes and prints a factorial
 *
 * The first argument is integer used for computing the factorial
 * @NB: Factorial of NaN is 1
 * @NB: You must do it recursively
 * @NB: You must use a function
 * @NB: You must use console.log(...) to print all output
 * @NB: You are not allowed to use var
 */

/**
 * factorial - computes a factorial of a number
 * @a: number, number
 *
 * Return: !n, number or Infinity or 1 (if NaN)
 */
function factorial (n) {
  if (isNaN(Number(n)) || n === 1) {
    return 1;
  }

  return factorial(n - 1) * n;
}

console.log(factorial(process.argv[2]));
