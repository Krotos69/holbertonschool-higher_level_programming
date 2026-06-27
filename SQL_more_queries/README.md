Perfect, Krotos — here is a **Holberton‑style `README.md`**, clean, structured, and matching the format used in school projects.  
It uses only the concepts you asked for, and it is fully Markdown‑ready.

---

# **SQL - More queries**

# 0x0D. MySQL – Users, Privileges & Relational Concepts  




## **Description**
This project introduces essential MySQL concepts used in real relational database design and administration.  
You will learn how to create users, manage privileges, define constraints, and retrieve data across multiple tables using JOINs and subqueries.

---

## **Learning Objectives**
By the end of this project, you should be able to explain, without Google:

### ✔ **How to create a new MySQL user**
- Use `CREATE USER 'user'@'host' IDENTIFIED BY 'password';`
- Example:  
  ```sql
  CREATE USER 'bob'@'localhost' IDENTIFIED BY 'mypassword';
  ```

### ✔ **How to manage privileges for a user**
- Use `GRANT`, `REVOKE`, and `SHOW GRANTS`.
- Example:  
  ```sql
  GRANT SELECT, INSERT ON mydb.* TO 'bob'@'localhost';
  ```

### ✔ **What is a PRIMARY KEY**
- Uniquely identifies each row.
- Cannot be NULL.
- Example:  
  ```sql
  id INT PRIMARY KEY
  ```

### ✔ **What is a FOREIGN KEY**
- Links a column to a primary key in another table.
- Enforces referential integrity.
- Example:  
  ```sql
  FOREIGN KEY (author_id) REFERENCES authors(id)
  ```

### ✔ **How to use NOT NULL and UNIQUE constraints**
- `NOT NULL` → value required  
- `UNIQUE` → no duplicates  
- Example:  
  ```sql
  email VARCHAR(255) NOT NULL UNIQUE;
  ```

### ✔ **How to retrieve data from multiple tables**
- Use JOINs (INNER, LEFT, RIGHT, FULL).
- Example:  
  ```sql
  SELECT users.name, orders.total
  FROM users
  JOIN orders ON users.id = orders.user_id;
  ```

### ✔ **What are subqueries**
- A query inside another query.
- Example:  
  ```sql
  SELECT name
  FROM users
  WHERE id IN (SELECT user_id FROM orders);
  ```

### ✔ **What are JOIN and UNION**
- **JOIN** → combine rows horizontally  
- **UNION** → combine result sets vertically  
- Example JOIN:  
  ```sql
  SELECT * FROM a JOIN b ON a.id = b.id;
  ```
- Example UNION:  
  ```sql
  SELECT name FROM a
  UNION
  SELECT name FROM b;
  ```

---

## **Requirements**
- Allowed editors: `vi`, `vim`, `emacs`
- All SQL files tested on: **MySQL 8.0**
- SQL queries must start with uppercase keywords
- No semicolon at the end of comments
- Files must end with a new line

---

## **Usage**
Run SQL scripts using:

```bash
$ cat script.sql | mysql -hlocalhost -uroot -p
```

---

## **Author**
**Eugenio Martinez** — Holberton School  






































Here’s your **Holberton‑style study sheet** — short, clear, example‑driven, no fluff.

---

## ⭐ How to create a new MySQL user  
**Definition:** Use `CREATE USER` to add a new account.  
**Example (from docs):**  
> “CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';”   

**Short version:**  
```sql
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'mypassword';
```

---

## ⭐ How to manage privileges for a user  
**Definition:** Use `GRANT` to give permissions, `REVOKE` to remove.  
**Example (from docs):**  
> “GRANT INSERT ON classicmodels.* TO bob@localhost;”   

**Short version:**  
```sql
GRANT SELECT, INSERT ON mydb.* TO 'bob'@'localhost';
REVOKE INSERT ON mydb.* FROM 'bob'@'localhost';
```

---

## ⭐ What’s a PRIMARY KEY?  
**Definition:** A column that uniquely identifies each row. Cannot be NULL.  
**From docs:**  
> “The PRIMARY KEY constraint uniquely identifies each record…”   

**Example:**  
```sql
id INT PRIMARY KEY
```

---

## ⭐ What’s a FOREIGN KEY?  
**Definition:** A column that references a PRIMARY KEY in another table.  
**From docs:**  
> “A FOREIGN KEY in one table points to a PRIMARY KEY in another table.”   

**Example:**  
```sql
author_id INT,
FOREIGN KEY (author_id) REFERENCES authors(id)
```

---

## ⭐ NOT NULL & UNIQUE constraints  
**NOT NULL:** Column cannot store NULL.  
**UNIQUE:** No duplicate values allowed.  
**From docs:**  
> “A column with a NOT NULL constraint cannot have NULL values.”  
> “The UNIQUE constraint ensures that all data are unique…”   

**Example:**  
```sql
email VARCHAR(255) NOT NULL UNIQUE
```

---

## ⭐ How to retrieve data from multiple tables  
**Use JOIN** (most common).  
**Example:**  
```sql
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id;
```

---

## ⭐ What are subqueries?  
**Definition:** A query inside another query.  
**From docs:**  
> “Subqueries should be aligned… sometimes nested.”   

**Example:**  
```sql
SELECT name
FROM users
WHERE id IN (SELECT user_id FROM orders);
```

---

## ⭐ What are JOIN and UNION?  
### JOIN  
Combine rows from multiple tables based on a related column.  
**Example (INNER JOIN):**  
```sql
SELECT * FROM table1
INNER JOIN table2 ON table1.id = table2.id;
```

### UNION  
Stack results vertically (same number of columns).  
**Example:**  
```sql
SELECT name FROM table1
UNION
SELECT name FROM table2;
```

---

If you want, I can turn this into a **flashcard set** or a **practice quiz**.