#!/usr/bin/node
const dict = require('./101-data').dict;

const result = {};
for (const key in dict) {
  if (dict[key] in result) {
    result[dict[key]].push(key);
  } else {
    result[dict[key]] = [key];
  }
}

console.log(result);
