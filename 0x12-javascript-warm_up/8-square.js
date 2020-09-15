#!/usr/bin/node
const arg = process.argv[2];

if (isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  for (let row = 0; row < Number(arg); row++) {
    let sqr = '';
    for (let col = 0; col < Number(arg); col++) {
      sqr += 'X';
    }
    console.log(sqr);
  }
}
