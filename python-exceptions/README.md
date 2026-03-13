
---

# **Python – Exceptions**

##   **Project Description**
This document provides a clear and practical explanation of how *exceptions* work in Python, when to use them, how to handle them properly, and how to integrate them into a program to improve robustness and readability.

---

##   **Project Purpose**
The purpose of this guide is to offer a simple yet complete introduction to exception handling in Python, especially useful for beginners or developers who want to strengthen their foundational knowledge.

---

##   **Problem Solved**
Incorrect error handling can lead to unexpected crashes, data loss, or abrupt interruptions.  
This document helps you:

- Understand the difference between errors and exceptions  
- Handle failures in a controlled way  
- Write safer and more professional code  

---

##   **General Context**
Python uses an exception-handling system to manage unexpected situations during program execution.  
Understanding this system is essential for building reliable and easy-to-debug applications.

---

##   **Definition**

### **Errors**
Issues that prevent the program from running correctly, such as syntax or indentation errors.

### **Exceptions**
Unexpected events that occur during execution and can be *caught* and *handled* to prevent the program from crashing.

---

##   **Usage**
Exceptions are handled using the following keywords:

- `try`
- `except`
- `else`
- `finally`
- `raise`

Basic example:

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("You must enter a valid number.")
```

---

## 💻 **Command Examples**

### **Catching a specific exception**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### **Catching multiple exceptions**
```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("A value or type error occurred.")
```

### **Using `else`**
```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
```

### **Using `finally` for cleanup**
```python
try:
    file = open("data.txt")
    data = file.read()
except Exception:
    print("An error occurred.")
finally:
    file.close()
```

### **Raising an exception**
```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
```

---

##   **Basic Use Cases**

- Input validation  
- File handling  
- Database connections  
- Network operations  
- Control flow in complex programs  
- Resource cleanup (files, sockets, memory)  

---

##   **Credits / Authors**
**Author:**  
**Eugenio Martínez**

---
