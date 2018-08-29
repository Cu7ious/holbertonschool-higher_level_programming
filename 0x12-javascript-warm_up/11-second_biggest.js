#!/usr/bin/node
/**
 * This script searches the second biggest integer in the list of arguments
 *
 * You can assume all arguments can be converted to integer
 * If no argument passed, prints 0
 * If the number of arguments is 1, print 0
 * @NB: You must use console.log(...) to print all output
 * @NB: You are not allowed to use var

 * @NB: You are not allowed to use var
 */

/**
 * secondBiggest - computes a factorial of a number
 * @NB: assumes array of arguments as an input
 *
 * Return: second biggest number of NaN
 */
function secondBiggest () {
  if (!arguments[0] || arguments[0].length <= 1) {
    return 0;
  }

  arguments[0].splice(arguments[0].indexOf(String(Math.max(...arguments[0]))), 1);
  return Math.max(...arguments[0]);
}

console.log(secondBiggest(process.argv.slice(2)));
