# SQL
- SQL是一种数据库管理系统，用于管理数据库，是一种声明式编辑语言。
  - 声明式：SQL语言的核心思想是声明式，即告诉数据库应该做什么，而不是如何做。
## SQL基础语法
### 创建/删除数据库新表
- select语句:用于创建新表或从已有表中检索数据。
- 语法：select语句包括一个以逗号分隔的列描述列表。列描述是一个表达式，可选择性加上名称:`select [expression] as [column_name], [expression] as [column_name],  `
- select语句还有许多子句，`from`子句指定要从哪个表中检索数据，`where`子句指定过滤条件，`order by`子句指定排序条件。
- select语句可以创建一行的表，用union语句可以联合多个select语句的结果，只能对具有相同列数和每列中数据类型相同的表进行union操作，union操作的结果表的列名和数据类型由第一个select语句的结果决定。
- 创建表：`create table table_name as [select_statement]`
- 列表中的数据也可以进行算术运算。
```sql
create table table_name as
select column1 + column2 as sum_of_columns, column3 - column4 as difference
from table1;
```
- 创建新表时也可以直接指定列名并对其进行约束。
- 约束包括`not null`（非空约束）、`unique`（唯一约束）、`default`（默认值约束）等等。
```sql
create table numbers (n, note);
create table numbers (n UNIQUE, note); -- 唯一约束
create table numbers (n , note DEFAULT 'unknown'); -- 默认值约束
```
- 删除表：`drop table (if exists) table_name `
## 表的连接
- select语句可以连接多个表，语法为`select column_name from table1, table2 where condition`。
- 连接的表必须具有相同的列数和数据类型。
- 连接的表可以有不同的列名，但必须具有相同的数据类型。
- 连接表会列出所有可能的组合。
- 当你连接一张表与其自身时，你可以使用别名与点表达式来区分不同的表。
```sql   
create table table_name as
select a.column1, b.column2 from table1 as a, table1 as b where a.id = b.id;
```
## 数字表达式
- SQL支持常见的数学表达式，也有许多内置函数：
  - 算术运算符：`+ - * / %`
  - 位运算符：`& | ^ ~ << >>`
  - 比较运算符：`= <> > < >= <= !=`
  - 逻辑运算符：`and or not`
  - 聚合函数：`sum avg max min count`
     - count 函数可以统计行数，count(*)统计所有行数，count（distict column_name）统计指定列的不重复的行数。
     - 在选择和聚合同时使用时，小心使用聚合函数，如数据的avg值可能不对应数据表中的任何一行，可能有很多行对应max值，但应用max函数时，可能只会返回一个值。
```sql
create table ex as
select 5 as num , 'a' as char union
select 10 as num, 'b' as char union
select 15 as num, 'c' as char union
select 5 as num , 'd' as char;
select max(num) from ex;
> 15
select min(num), char from ex;
> 5|a
select avg(num), char from ex;
> 8.75|a
```

## 字符串表达式
- SQL支持字符串表达式，包括字符串连接、比较、匹配、替换、提取子串等。
- 字符串连接：`||`
```sql
select 'Hello, ' || 'World';
> 'Hello, World'
```
- 提取子串：`substr(string, start, length)`
```sql
select substr('Hello World', 6, 5);
> 'World'
```
## 分组
- SQL支持分组，可以对结果集进行分组，并对分组进行聚合操作。
- 分组的语法为`group by column_name`（也可以对多列进行分组），聚合的语法为`select column_name, aggregate_function(column_name) from table_name group by column_name`。
```sql
create table ex as
select 5 as num, 'a' as char union
select 10 as num, 'b' as char union
select 10 as num, 'c' as char union
select 5 as num, 'd' as char union
select  5 as num , 'e' as char;

select num,count(*) from ex group by num;
5|3
10|2

select num, max(char) from ex group by num;
5|e
10|c
```
- having子句可以对分组后的结果进行过滤。
```sql
select num, count(*) from ex group by num having count(*) > 2;
5|3
```
## 更改表
- SQL支持对表进行插入、更新、删除操作。
- 插入：`insert into table_name (column1, column2,...) values (value11, value12, ...) ,(value21, value22, ...)...`
- 更新：`update table_name set column1 = value1, column2 = value2,... where condition`
- 删除：`delete from table_name where condition`
- 注意：更新和删除操作必须有where子句，否则会对整个表进行操作。
## Python中的SQL
- 在Python中，可以使用`sqlite3`模块来连接到SQLite数据库，并执行SQL语句。
```python
import sqlite3
# 连接到SQLite数据库
conn = sqlite3.connect('mydatabase.db')
# 执行SQL语句
conn.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
conn.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
conn.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")
conn.execute("INSERT INTO students (name, age) VALUES ('Charlie', 21)")
# 提交事务
conn.commit()
# 关闭连接
conn.close()
```