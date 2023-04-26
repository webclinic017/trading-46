'use strict';

/////////////////
const PORT = 8080;

const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'dist')));

app.get('/*', function(req, res) {
   // res.setHeader('Content-Type', 'application/javascript');
   res.sendFile(path.join(__dirname, 'dist' , 'index.html'));
});

app.listen(PORT, () => {
   console.log('Server started...');
});
