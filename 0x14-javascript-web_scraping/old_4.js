#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count;
let result;
let item;

request(url, function (error, response, body) {
  if (error) {
    console.log('code: 404');
  } else {
    // characters = JSON.parse(body).characters
    result = JSON.parse(body).results;
    count = 0
    for (item of result) {
      for (character in item.characters) {
	if ('https://swapi-api.hbtn.io/api/people/18/' === character) {
        count = count + 1;
	console.log(count);
	    }
      }
    }
    console.log(count);
  }
});
