#!/usr/bin/node
exports.converter = function (base) {
  function InternConv (n) {
    return n.toString(base);
  }
  return InternConv;
};
