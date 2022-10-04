#!/usr/bin/node
exports.esrever = function (list) {
  let result = []
  for (i in list) {
    result.push(list.pop());
  }
  console.log(result);
}
