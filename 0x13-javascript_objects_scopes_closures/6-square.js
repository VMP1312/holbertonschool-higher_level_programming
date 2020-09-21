#!/usr/bin/node
const SquareBase = require('./5-square.js');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let cnt = 0; cnt < this.width; cnt++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
