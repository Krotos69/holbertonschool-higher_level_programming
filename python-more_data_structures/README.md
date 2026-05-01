
---

```markdown
# Python – More Data Structures: Set, Dictionary

## 📝 Resume
This project explores two essential Python data structures: **sets** and **dictionaries**.  
You will learn what they are, how they work, how to iterate through them, and when to use each one.  
The project also introduces **lambda functions** and the functional programming tools **map**, **filter**, and **reduce**.

---

## ⭐ Characteristics

### 🔷 Sets
- Store **unique** items (no duplicates)
- **Unordered** (no indexing)
- Very **fast** membership checking (`in`)
- Support mathematical operations like union, intersection, and difference

### 🟨 Dictionaries
- Store data in **key–value pairs**
- Keys must be **unique** and **immutable**
- Values can be any type
- Ideal for structured or labeled data

### ⚡ Lambda Functions
- Small, anonymous functions
- Useful for short, simple operations

### 🧠 map(), filter(), reduce()
- **map()** → applies a function to each item  
- **filter()** → keeps items that satisfy a condition  
- **reduce()** → reduces a list to a single value (sum, product, etc.)

---

## 🧪 Demo / Examples

### ✔ Set Example
```python
my_set = {1, 2, 3, 3}
print(my_set)  # {1, 2, 3}

my_set.add(4)
my_set.update([5, 6])
print(my_set)
```

### ✔ Dictionary Example
```python
student = {
    "name": "Ana",
    "age": 21,
    "school": "Holberton"
}

print(student["name"])  # Ana
```

### ✔ Iterating Through a Set
```python
for item in my_set:
    print(item)
```

### ✔ Iterating Through a Dictionary
```python
for key, value in student.items():
    print(key, value)
```

### ✔ Lambda + map()
```python
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
# [2, 4, 6]
```

### ✔ Lambda + filter()
```python
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2]
```

### ✔ Lambda + reduce()
```python
from functools import reduce

total = reduce(lambda a, b: a + b, nums)
# 6
```

---

## 📘 Usage & Definitions

### 🔷 When to Use Sets
Use a **set** when:
- You need **unique** items
- You don’t care about order
- You need fast membership checks (`if x in set`)

### 🔷 When to Use Dictionaries
Use a **dictionary** when:
- You need to store **labeled** or **structured** data
- You want fast access using keys
- You need to represent objects or records

### 🔧 Installation
No installation required — sets, dictionaries, lambda, map, filter, and reduce are **built into Python**.

Check your Python version:

```bash
python3 --version
```

---

## 📄 License
This README is for educational purposes and does not include a specific license unless added by the project owner.

---

## 👤 Author
**Eugenio Martinez**
```

---
