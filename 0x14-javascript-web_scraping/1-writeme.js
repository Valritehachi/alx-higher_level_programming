#!/usr/bin/node

// a write me file

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
