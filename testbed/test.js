const duckdb = require('duckdb');

const db = new duckdb.Database(':memory:');  // 或提供文件名，如 'test.db'
const conn = db.connect();
conn.run("CREATE TABLE test (a INTEGER, b STRING)");
conn.run("INSERT INTO test VALUES (42, 'hello'), (7, 'world')");

conn.all("SELECT * FROM test", function(err, rows) {
  if (err) throw err;
  console.log(rows);  // [ { a: 42, b: 'hello' }, { a: 7, b: 'world' } ]
});
