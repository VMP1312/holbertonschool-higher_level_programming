#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const element in list) {
    if (list[element] === searchElement) {
      cnt++;
    }
  }
  return cnt;
};
