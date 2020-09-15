#!/usr/bin/node
const fst = Number(process.argv[2]);
const scd = Number(process.argv[3]);

add(fst, scd);

function add (a, b) {
  console.log(a + b);
}
