#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
let url = `https://swapi-api.hbtn.io/api/films/${id}`

request(url, function (error, response, body) {
  error ? console.log('code: 404') : console.log(JSON.parse(body) && JSON.parse(body).title);
});
