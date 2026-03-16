
---

#    Python - Object-relational mapping
#    Python + MySQL + ORM — Study Guide README

##    Overview
This README explains the fundamentals of working with MySQL from Python and introduces the concept of Object‑Relational Mapping (ORM).  
It covers:

- Connecting to a MySQL database  
- Selecting rows  
- Inserting rows  
- Understanding ORM  
- Mapping Python classes to MySQL tables  

Each section is written in a study‑mode style to help you understand the concepts, not just memorize them.

---

##    1. Connecting to a MySQL Database from Python

To communicate with MySQL, Python needs a **connector** — a tool that acts like a translator between Python and the database.

### ✔ Key Concepts
- Install a MySQL driver (e.g., `mysql-connector-python`)
- Provide connection details:
  - host  
  - username  
  - password  
  - database name  
- Create a **cursor** to execute SQL commands

### ✔ Example
```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword",
    database="school"
)

cursor = db.cursor()
```

**Think of it like:**  
`db` = the door to the database  
`cursor` = the hand that performs actions inside the database  

---

##    2. Selecting Rows from a MySQL Table

A **SELECT** query is used to *read* data from the database.

### ✔ Key Concepts
- `cursor.execute()` sends the SQL query
- `fetchall()` retrieves all rows
- `fetchone()` retrieves one row
- Loop through results to use them

### ✔ Example
```python
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

**Think of it like:**  
You ask the database a question, and it returns a list of answers.

---

## ➕ 3. Inserting Rows into a MySQL Table

An **INSERT** query adds new data to a table.

### ✔ Key Concepts
- Use placeholders (`%s`) to safely insert values
- After inserting, call `db.commit()` to save changes

### ✔ Example
```python
sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
values = ("Ana", 20)

cursor.execute(sql, values)
db.commit()
```

**Think of it like:**  
`commit()` is the “Save” button — without it, nothing is stored.

---

##    4. What ORM Means

**ORM = Object‑Relational Mapping**

It allows you to interact with a database using **Python classes instead of SQL queries**.

### ✔ Why It Matters
- You write Python code, not SQL
- Cleaner and safer
- Easier to maintain
- Automatically handles SQL behind the scenes

### ✔ Example Idea
Instead of writing:
```sql
SELECT * FROM users;
```

You write:
```python
User.query.all()
```

---

##    5. Mapping a Python Class to a MySQL Table (Using SQLAlchemy)

In ORM, a **class** represents a **table**, and each **attribute** represents a **column**.

### ✔ Key Concepts
- Define a class (e.g., `User`)
- Assign a table name
- Define columns using SQLAlchemy types
- ORM creates the table automatically

### ✔ Example
```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
```

**Think of it like:**  
The class is the blueprint.  
The ORM uses that blueprint to build the actual table in MySQL.

---

##    Summary Table

| Topic | What You Should Understand |
|-------|-----------------------------|
| Connect to MySQL | Python needs a connector + credentials |
| SELECT rows | Use SQL + fetch methods to read data |
| INSERT rows | Use SQL + commit to save data |
| ORM | Python objects instead of SQL |
| Class → Table | Class = table, attributes = columns |

---

##    Author
-  Eugenio Martinez
