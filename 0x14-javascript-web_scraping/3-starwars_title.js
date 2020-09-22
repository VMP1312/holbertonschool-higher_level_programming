#!/usr/bin/node
const request = require('request');
const MovieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + MovieID;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const fetched = JSON.parse(body);
    console.log(fetched.title);
  }
});
