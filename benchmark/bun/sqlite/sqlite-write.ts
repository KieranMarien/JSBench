import { Database } from "bun:sqlite";

const db = new Database("bun.sqlite");
db.run(
 "create table students (id int, name varchar(255), age int, grade int)"
);
db.run("insert into students values(1, 'John', 6, 1)");
db.query("select * from students").all();

db.run('drop table students')

db.close()

