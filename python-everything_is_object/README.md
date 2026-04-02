
---

```markdown
# Python - Everything is an Object

##    Objective
The objective of this document is to provide a clear and concise understanding of one of Python’s core principles: **everything is an object**.  
This concept is fundamental to how Python handles variables, memory, mutability, and function behavior.  
Understanding these ideas is essential for writing efficient, predictable, and bug‑free Python code.

---

##    Table of Contents
1. What is an object?
2. Difference between a class and an object (instance)
3. Difference between immutable and mutable objects
4. What is a reference?
5. What is an assignment?
6. What is an alias?
7. How to know if two variables are identical
8. How to know if two variables are linked to the same object
9. How to display the variable identifier (memory address)
10. What is mutable and immutable?
11. Built‑in mutable types
12. Built‑in immutable types
13. How Python passes variables to functions

---

##   Topic

### 1. What is an object?
An object is a Python entity with **identity**, **type**, and **value**.

### 2. What is the difference between a class and an object or instance?
A **class** is a blueprint; an **object/instance** is a concrete realization of that blueprint.

### 3. What is the difference between immutable object and mutable object?
- **Immutable**: cannot change after creation  
- **Mutable**: can change in place

### 4. What is a reference?
A reference is the link between a variable name and the object stored in memory.

### 5. What is an assignment?
Assignment binds a variable name to an object reference.

### 6. What is an alias?
Two variables referencing the **same object**.

### 7. How to know if two variables are identical?
Using the `is` operator.

### 8. How to know if two variables are linked to the same object?
Also using the `is` operator.

### 9. How to display the variable identifier (memory address)?
Using the built‑in function `id()`.

### 10. What is mutable and immutable?
- **Mutable**: object can change internally  
- **Immutable**: object cannot change; any modification creates a new object

### 11. What are the built‑in mutable types?
`list`, `dict`, `set`, `bytearray`, `memoryview`

### 12. What are the built‑in immutable types?
`int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`

### 13. How does Python pass variables to functions?
Python uses **pass‑by‑object‑reference** (also known as pass‑by‑assignment).

---

##    Summary
Python treats **everything as an object**, meaning every value has a type, identity, and behavior.  
Variables do not store data directly; they store **references** to objects in memory.  
Understanding the difference between **mutable** and **immutable** types is crucial, as it affects how data behaves when passed to functions or assigned to new variables.  
Identity checks using `is`, memory inspection with `id()`, and awareness of aliasing help developers avoid unintended side effects.  
This knowledge forms the foundation for mastering Python’s memory model and writing robust, predictable programs.

---

##    Author
**Eugenio Martinez**
```

---
