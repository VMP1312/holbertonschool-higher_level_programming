#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${body.statusCode}`);
  }
});
