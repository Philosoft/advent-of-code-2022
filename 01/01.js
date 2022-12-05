'use strict';

const fs = require('fs');

const buf = fs.readFileSync('input.txt');
console.log(String(buf));