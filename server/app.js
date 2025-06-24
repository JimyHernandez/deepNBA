const express = require('express');
const cors = require('cors')
let app = express();

app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
    res.send('Hello World')
})

module.exports = app;

