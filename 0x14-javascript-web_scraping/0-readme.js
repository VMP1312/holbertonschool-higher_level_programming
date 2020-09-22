#!/usr/bin/node
const myFile = process.argv[2];
const fs = require('fs');

fs.readFile(myFile, 'utf-8', (err, rd) => {
  if (err) {
    console.log(err);
  } else {
    console.log(rd);
  }
});
