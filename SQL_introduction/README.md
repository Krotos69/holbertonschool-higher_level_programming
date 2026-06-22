
---

```markdown
# SQL Introduction – Learning the Foundations of Relational Databases

##   Introduction of SQL – Introduction
Structured Query Language (SQL) is the standard language used to interact with relational databases.  
It allows developers and data professionals to create databases, define their structure, store information, and retrieve it efficiently.  
SQL is essential in backend development, data engineering, analytics, and any system that relies on structured data.

This project introduces the core concepts of SQL and MySQL, including:
- What databases and relational databases are  
- How SQL works  
- How to create and manage databases and tables  
- How to manipulate and query data  
- How to use MySQL functions and subqueries  

---

##   Project Vision and Scope
The goal of this project is to build a strong foundation in SQL by learning how relational databases operate and how to interact with them using MySQL.

This project covers:
- Understanding databases and relational models  
- Learning SQL syntax and core commands  
- Creating and modifying databases and tables  
- Performing CRUD operations (Create, Read, Update, Delete)  
- Writing efficient SELECT queries  
- Using subqueries for advanced data retrieval  
- Applying MySQL built‑in functions for strings, numbers, and dates  

By the end of this project, you will be able to:
- Design basic database structures  
- Write SQL queries confidently  
- Understand how data is stored, related, and retrieved  
- Use MySQL as a practical tool for real‑world applications  

---

##   Learning Objectives
By completing this project, you will be able to:

### **1. Understand Core Concepts**
- Define what a database is  
- Explain what a relational database is  
- Understand SQL and its purpose  
- Describe what MySQL is and how it works  

### **2. Work with Database Structures**
- Create a database in MySQL  
- Understand DDL (Data Definition Language)  
- Create and alter tables using SQL commands  

### **3. Manipulate and Query Data**
- Use DML (Data Manipulation Language)  
- SELECT data from tables using filters, sorting, and limits  
- INSERT new records  
- UPDATE existing records  
- DELETE records safely  

### **4. Write Advanced SQL**
- Use subqueries inside SELECT, WHERE, and HAVING clauses  
- Apply MySQL functions (string, numeric, date, aggregate)  
- Combine SQL features to solve real data problems  



#    SQL Basics — Holberton Study Guide  
A complete introduction to SQL, relational databases, and MySQL commands.  
This guide covers essential concepts and includes examples for each topic.

---

##    Table of Contents
- [What is a Database?](#what-is-a-database)
- [What is a Relational Database?](#what-is-a-relational-database)
- [What does SQL stand for?](#what-does-sql-stand-for)
- [What is MySQL?](#what-is-mysql)
- [How to Create a Database](#how-to-create-a-database)
- [DDL vs DML](#ddl-vs-dml)
- [How to Create or Alter a Table](#how-to-create-or-alter-a-table)
- [How to Select Data](#how-to-select-data)
- [How to Insert, Update, Delete Data](#how-to-insert-update-delete-data)
- [What are Subqueries?](#what-are-subqueries)
- [Using MySQL Functions](#using-mysql-functions)

---

##    What is a Database?
A **database** is an organized collection of data stored electronically.  
It allows efficient storage, retrieval, and management of information.

### Example  
A school database may contain:
- `students` table  
- `courses` table  
- `grades` table  

---

##    What is a Relational Database?
A **relational database (RDBMS)** stores data in **tables** and uses **relationships** between them.  
Tables are linked using **primary keys (PK)** and **foreign keys (FK)**.

### Example  
```
students(id PK, name)
enrollments(id PK, student_id FK → students.id)
```

---

##    What does SQL stand for?
**SQL = Structured Query Language**  
It is the standard language used to interact with relational databases.

---

##    What is MySQL?
MySQL is an **open‑source relational database management system**.  
It uses SQL to store, retrieve, and manage data.

---

##    How to Create a Database
Use the `CREATE DATABASE` statement.

### Example  
```sql
CREATE DATABASE holberton_school;
```

---

##    DDL vs DML

### **DDL — Data Definition Language**
Used to define or modify database structures.

Commands:
- `CREATE`
- `ALTER`
- `DROP`

### **DML — Data Manipulation Language**
Used to manipulate data inside tables.

Commands:
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

---

##    How to Create or Alter a Table

### Create a Table  
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    email VARCHAR(100) UNIQUE
);
```

### Alter a Table  
Add a column:
```sql
ALTER TABLE students ADD COLUMN grade FLOAT;
```

Modify a column:
```sql
ALTER TABLE students MODIFY age SMALLINT;
```

Drop a column:
```sql
ALTER TABLE students DROP COLUMN grade;
```

---

##    How to Select Data

### Select all rows  
```sql
SELECT * FROM students;
```

### Select specific columns  
```sql
SELECT name, age FROM students;
```

### With conditions  
```sql
SELECT * FROM students WHERE age > 20;
```

### With sorting  
```sql
SELECT * FROM students ORDER BY age DESC;
```

---

##    How to Insert, Update, Delete Data

### INSERT  
```sql
INSERT INTO students (name, age)
VALUES ('Alice', 22);
```

### UPDATE  
```sql
UPDATE students
SET age = 23
WHERE name = 'Alice';
```

### DELETE  
```sql
DELETE FROM students
WHERE name = 'Alice';
```

---

##    What are Subqueries?
A **subquery** is a query inside another query.  
Used for comparisons, filtering, or generating temporary results.

### Example  
Students older than the average age:
```sql
SELECT name
FROM students
WHERE age > (SELECT AVG(age) FROM students);
```

---

##    Using MySQL Functions

### Aggregate  
```sql
SELECT COUNT(*) FROM students;
```

### String  
```sql
SELECT UPPER(name) FROM students;
```

### Date  
```sql
SELECT NOW();
```

### Conditional  
```sql
SELECT IF(age > 18, 'Adult', 'Minor') FROM students;
```

---

## ✅ Author
**Eugenio Martinez** — Holberton School Student  
SQL Study Guide for learning and practice.

---
