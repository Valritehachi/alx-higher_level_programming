#!/usr/bin/node

// a code to check the status

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
