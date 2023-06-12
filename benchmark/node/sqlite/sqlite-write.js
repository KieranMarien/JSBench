const Database = require('better-sqlite3');

const db = new Database('node.sqlite');

db.prepare(
  "create table students (id int, name varchar(255), age int, grade int)"
).run();

db.prepare("insert into students values(1, 'John', 6, 1)").run();

db.prepare('drop table students').run();

db.close()