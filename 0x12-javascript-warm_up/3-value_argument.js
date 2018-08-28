#!/usr/bin/node
/**
 * This script prints the first argument passed to it:
 *
 * If no arguments are passed to the script: "No argument"
 * NB: You are not allowed to use length
 */
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
