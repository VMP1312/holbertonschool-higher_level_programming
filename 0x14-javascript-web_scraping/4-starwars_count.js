#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = '18';

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let cnt = 0;
    for (const movie in data) {
      const chars = data[movie].characters;
      for (const mv in chars) {
        if (chars[mv].includes(id)) {
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
});
