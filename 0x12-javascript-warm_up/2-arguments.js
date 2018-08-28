#!/usr/bin/node
/**
 * This script prints a message depending of the number of arguments passed:
 *
 * If no arguments are passed to the script: "No argument"
 * If only one argument is passed to the script: "Argument found"
 * Otherwise: "Arguments found"
 */
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
