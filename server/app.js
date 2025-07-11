const express = require('express');
const cors = require('cors')
let app = express();

app.use(cors())
app.use(express.json())
app.use(express.static('client/public'));


app.get('/', (req, res) => {
    res.sendFile('index.html', {root: './client/views'});
})

module.exports = app;
