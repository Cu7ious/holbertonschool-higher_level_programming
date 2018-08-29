#!/usr/bin/node
/**
 * This module exports the 'add' function
 *
 * @NB: The function must be visible from outside
 * @NB: The name of the function must be 'add'
 * @NB: You are not allowed to use var
 */

/**
 * add - adds its arguments
 * @a: first summand, Number
 * @b: second summand, Number
 *
 * Return: sum a + b or Infinity.
 * If type of one of the arguments is wrong: NaN
 */
function add (a, b) {
  return Number(a) + Number(b);
}

module.exports = { add };
