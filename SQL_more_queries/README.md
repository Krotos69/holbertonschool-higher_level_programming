

---

```markdown
# MySQL Basics Cheat Sheet

This document provides a clear overview of essential MySQL concepts, including user management, privileges, keys, constraints, and querying techniques. It is designed as a quick reference for beginners and intermediate users.

---

##   Creating a New MySQL User

A MySQL user consists of a username, host, and password. Creating a user does **not** automatically grant permissions.

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

**Host options:**
- `localhost` — user can connect only from the same machine  
- `%` — user can connect from any host  
- `192.168.1.%` — restrict to a specific subnet  

---

##   Managing User Privileges

Privileges determine what actions a user can perform.

### Grant privileges on a database
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```

### Grant privileges on a specific table
```sql
GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO 'username'@'localhost';
```

### Remove privileges
```sql
REVOKE UPDATE ON database_name.table_name FROM 'username'@'localhost';
```

### Apply changes
```sql
FLUSH PRIVILEGES;
```

---

##   PRIMARY KEY

A **PRIMARY KEY** uniquely identifies each row in a table.

- Must be unique  
- Cannot be NULL  
- One per table (can be composite)

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    username VARCHAR(50),
    PRIMARY KEY (id)
);
```

---

##   FOREIGN KEY

A **FOREIGN KEY** links two tables and enforces referential integrity.

```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT,
    user_id INT,
    product VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

Optional cascading actions:

```sql
ON DELETE CASCADE
ON UPDATE CASCADE
```

---

##   NOT NULL and UNIQUE Constraints

### NOT NULL
Ensures a column always has a value.

```sql
email VARCHAR(255) NOT NULL
```

### UNIQUE
Ensures all values in the column are different.

```sql
email VARCHAR(255) UNIQUE
```

### Combined
```sql
email VARCHAR(255) NOT NULL UNIQUE
```

---

##   Retrieving Data from Multiple Tables

Use **JOINs** to combine related data.

```sql
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id;
```

**JOIN types:**  
- `INNER JOIN` — only matching rows  
- `LEFT JOIN` — all rows from left table + matches  
- `RIGHT JOIN` — all rows from right table + matches  
- `CROSS JOIN` — Cartesian product  

---

##   Subqueries

A subquery is a query inside another query.

```sql
SELECT name
FROM users
WHERE id IN (SELECT user_id FROM orders);
```

Subqueries can appear in:
- `SELECT`
- `FROM`
- `WHERE`
- `HAVING`

---

##   JOIN vs UNION

### JOIN
Combines **columns** from related tables.

```sql
SELECT u.name, o.product
FROM users u
JOIN orders o ON u.id = o.user_id;
```

### UNION
Combines **rows** from multiple queries.

```sql
SELECT name FROM customers
UNION
SELECT name FROM suppliers;
```

`UNION ALL` keeps duplicates.

---

##   Summary

This guide covers:
- Creating users  
- Managing privileges  
- Primary & foreign keys  
- Constraints  
- JOINs & subqueries  
- UNION operations  

Use this as a quick reference when working with MySQL databases.
```

---

