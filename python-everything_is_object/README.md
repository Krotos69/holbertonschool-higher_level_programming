            **Python - Everything is object**

---

```markdown
# Python - Everything is object

## Project Overview
This project provides a clear, structured explanation of fundamental Python concepts related to objects, mutability, references, identity, and function behavior. The goal is to help learners understand how Python handles data internally, how variables interact with objects, and how mutability affects program behavior.

---

## Core Questions and Explanations

### 1. What is an object?
An **object** is a region of memory that stores data and provides associated behavior. In Python, *everything* is an object—numbers, strings, lists, functions, and even classes.

> “Variables in Python refer to **objects**.”

**Example:**
```python
x = [1, 2, 3]   # x refers to a list object
```

---

### 2. What is the difference between a class and an object or instance?
A **class** is a blueprint that defines attributes and behavior.  
An **object** (or **instance**) is a concrete realization of that class.

> “Classes represent kinds of values and **instances** combine data with methods.”

**Example:**
```python
class Dog:
    pass

fido = Dog()   # fido is an instance of class Dog
```

---

### 3. What is the difference between immutable object and mutable object?
- **Immutable objects** cannot be changed after creation.  
- **Mutable objects** can be modified in place.

> “Immutable objects cannot be changed ‘in place,’ whereas mutable objects can be modified.”

**Example:**
```python
s = "hello"
s += "!"        # creates a NEW string (immutable)

lst = [1, 2]
lst.append(3)   # modifies the SAME list (mutable)
```

---

### 4. What is a reference?
A **reference** is the association between a variable name and an object in memory.

> “Variables in Python **refer to objects**.”

**Example:**
```python
a = [10, 20]   # a references a list object
```

---

### 5. What is an assignment?
Assignment **binds a variable name to an object**. It does *not* copy the object.

> “Assigning one list variable to another creates an alias.”

**Example:**
```python
a = [1, 2]
b = a   # assignment: b now refers to the same object as a
```

---

### 6. What is an alias?
An **alias** occurs when two variables refer to the **same object**.

> “Assigning one list variable to another creates an **alias** so changes via one name affect the other.”

**Example:**
```python
a = [1, 2]
b = a
b[0] = 99
print(a)   # [99, 2] — because a and b alias the same list
```

---

### 7. How to know if two variables are identical?
Use the **identity operator** `is`.

> “`is` tests whether two names refer to the **same object**.”

**Example:**
```python
a = [1, 2]
b = a
a is b     # True
```

---

### 8. How to know if two variables are linked to the same object?
Use `is`, or compare their `id()` values.

> “`is` tests object identity.”

**Example:**
```python
a = [1, 2]
b = a
id(a) == id(b)   # True
```

---

### 9. How to display the variable identifier (which is the memory address in the CPython implementation)?
Use the built‑in function **`id()`**.

> “A practical way to see this is with `id()`.”

**Example:**
```python
x = [1, 2, 3]
print(id(x))   # e.g., 140392847492112
```

---

### 10. What is mutable and immutable?
- **Mutable**: object can change in place (list, dict, set).  
- **Immutable**: object cannot change; operations create new objects (int, float, str, tuple).

> “Immutable built‑in types include numbers, strings, tuples… mutable built‑ins include list, dict, set…”

**Example:**
```python
# Mutable
lst = [1, 2]
lst.append(3)

# Immutable
t = (1, 2)
# t[0] = 9  # ERROR: tuple is immutable
```

---

### 11. What are the built-in mutable types?
From your sources:

> “Mutable built‑ins include **list, dict, set, bytearray**.”

**Example:**
```python
d = {"a": 1}
d["b"] = 2   # modifies the dictionary
```

---

### 12. What are the built-in immutable types?
From your sources:

> “Immutable built‑in types include **numbers, strings, tuples, frozenset, bytes**.”

**Example:**
```python
s = "hello"
s = s.upper()   # creates a NEW string
```

---

### 13. How does Python pass variables to functions?
Python uses **call‑by‑object-reference** (also called call‑by‑sharing).  
The function receives a **reference** to the object, not a copy.

> “Passing a list to a function passes a **reference**, so functions that modify their list parameters produce side effects.”

**Example:**
```python
def add_item(lst):
    lst.append(99)

a = [1, 2]
add_item(a)
print(a)   # [1, 2, 99]
```

---

## Resources Used
- [https://www.openbookproject.net/thinkcs/python/english2e/ch09.html](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html)  
- `https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types` [(stackoverflow.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fstackoverflow.com%2Fquestions%2F8056130%2Fimmutable-vs-mutable-types")  
- `https://composingprograms.com/pages/24-mutable-data.html` [(composingprograms.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fcomposingprograms.com%2Fpages%2F24-mutable-data.html")  

---

## Author
**Eugenio Martinez**
```

