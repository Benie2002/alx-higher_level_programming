#!/usr/bin/node
const dict = require('./101-data').dict;

const wholeList = Object.entries(dict);
const values = Object.values(dict);
const uniqValues = [...new Set(values)];
const newDict = {};
for (const uniqValue of uniqValues) {
  const list = [];
  for (const entry of wholeList) {
    if (entry[1] === uniqValue) {
      list.unshift(entry[0]);
    }
  }
  newDict[uniqValue] = list;
}
console.log(newDict);
