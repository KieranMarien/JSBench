import { DB } from "https://deno.land/x/sqlite/mod.ts";

const db = new DB('deno.sqlite')

db.query(
  "create table students (id int, name varchar(255), age int, grade int)"
);
db.query("insert into students values(1, 'John', 6, 1)");

db.query('drop table students')

db.close()