#!/usr/bin/node
let cnt = 0;
exports.callMeMoby = function (x, theFunction) {
  for (cnt = 0; cnt < x; cnt++) {
    theFunction();
  }
};
