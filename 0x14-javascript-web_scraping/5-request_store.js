#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];

request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
