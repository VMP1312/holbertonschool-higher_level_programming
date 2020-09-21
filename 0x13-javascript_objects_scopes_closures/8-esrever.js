#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let cnt = list.length - 1; cnt >= 0; cnt--) {
    reverse.push(list[cnt]);
  }
  return reverse;
};
