#!/usr/bin/node

const fs = require('fs');

let result;

fs.readFile(process.argv[2], (err, data1) => {
  if (err) {
    throw err;
  }

  fs.readFile(process.argv[3], (err, data2) => {
    if (err) throw err;

    result = data1 + data2;
    fs.writeFile(process.argv[4], result, (err) => {
      if (err) throw err;
    });

  });
});
