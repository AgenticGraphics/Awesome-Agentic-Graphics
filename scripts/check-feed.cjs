const fs = require('node:fs');
const path = require('node:path');
const {validate} = require('../assets/feed-validation.js');
const root=path.join(__dirname,'..');
validate(JSON.parse(fs.readFileSync(path.join(root,'data/daily-results.json'),'utf8')),JSON.parse(fs.readFileSync(path.join(root,'data/taxonomy-labels.json'),'utf8')));
console.log('Feed dates, records, taxonomy labels, and evidence links passed validation.');
