const sqlite3 = require('sqlite').verbose()
const path = require('path')

const dbPath = path.join(__dirname, 'nba_stats.db')

const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
      console.error('Error opening database:', err.message);
    } else {
      console.log('Connected to the SQLite database.');
    }
  });

module.exports = db;