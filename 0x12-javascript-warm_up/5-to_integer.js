#!/usr/bin/node
/**
 * This script prints "My number: <first argument converted in integer>"
 * if the first argument can be converted to an integer
 *
 * If the argument can’t be converted to an integer, print "Not a number"
 * @NB: You are not allowed to use try/catch
 */
if (Number(process.argv[2]) !== NaN) {
  console.log(Number(process.argv[2]));
} else {
  console.log('Not a number');
}
