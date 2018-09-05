#!/usr/bin/node

const dict = require('./101-data').dict;
const result = {};

for (let i in dict) {
  if (result[dict[i]] === undefined) {
    result[dict[i]] = [];
  }

  result[dict[i]].push(i);
}

console.log(result);
