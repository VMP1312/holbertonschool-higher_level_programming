#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { console.log(err); } else {
    const done = {};
    for (const task of body) {
      if (task.completed) {
        if (done[task.userId]) {
          done[task.userId] += 1;
        } else {
          done[task.userId] = 1;
        }
      }
    }
    console.log(done);
  }
});
