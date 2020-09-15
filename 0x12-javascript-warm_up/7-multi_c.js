#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(arg, 10)) {
  console.log('Missing number of occurrences');
} else {
  for (let cnt = 0; cnt < Number(arg); cnt++) {
    console.log('C is fun');
  }
}
