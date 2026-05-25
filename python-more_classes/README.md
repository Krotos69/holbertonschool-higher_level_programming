#   **Python - More Classes and Objects**

---

# **Python OOP Study Guide**

## **📘 Description and Purpose**
This document serves as a comprehensive study guide for understanding **Object‑Oriented Programming (OOP) in Python**.  
It explains core concepts such as classes, objects, attributes, methods, encapsulation, abstraction, properties, and more—each with clear explanations and simple examples.  
Its purpose is to support learners in mastering Python OOP fundamentals.

---

## **📑 Table of Contents**
- Usage
- Features
- Project Structure
- Technologies Used
- Contributor
- Python OOP Concepts

---

## **🚀 Usage**
Use this guide to:
- Study Python OOP concepts  
- Review before assessments or interviews  
- Practice writing classes and objects  
- Understand Pythonic conventions like properties and attribute lookup  

---

## **✨ Features**
- Clear explanations of all major OOP concepts  
- Simple, readable examples  
- Covers Pythonic best practices  
- Includes attribute lookup, `__dict__`, dynamic attributes, and properties  
- Beginner‑friendly structure  

---

## **📁 Project Structure**
```
README.md   # This study guide
src/        # (Optional) Add your Python OOP practice scripts here
```

---

## **🛠 Technologies Used**
- Python 3.x  
- Markdown  

---

# **📚 Python OOP Concepts (Detailed Study Notes)**

---

## **1. What is OOP?**
Object‑Oriented Programming organizes code into **objects** that combine data and behavior.

**Example:**
```python
class Car:
    def drive(self):
        print("The car is moving")
```

---

## **2. “First‑class everything”**
In Python, **everything is an object**—functions, classes, numbers, modules.

**Example:**
```python
def greet():
    print("Hello")

x = greet
x()
```

---

## **3. What is a class?**
A **class** is a blueprint for creating objects.

**Example:**
```python
class Dog:
    species = "Canine"
```

---

## **4. What is an object / instance?**
An **object** is a real, created version of a class.

**Example:**
```python
dog1 = Dog()
```

---

## **5. Difference between class and object**
| Class | Object |
|-------|--------|
| Blueprint | Actual created item |
| Defines attributes/methods | Holds real data |
| One class → many objects | Each object is unique |

---

## **6. What is an attribute?**
A variable stored inside a class or object.

**Example:**
```python
self.name = name
```

---

## **7. Public, protected, private attributes**
Python uses naming conventions:

| Type | Syntax | Meaning |
|------|--------|---------|
| Public | `name` | Accessible everywhere |
| Protected | `_name` | Internal use (convention) |
| Private | `__name` | Name‑mangled |

**Example:**
```python
class A:
    public = 1
    _protected = 2
    __private = 3
```

---

## **8. What is `self`?**
Refers to the **current instance**.

**Example:**
```python
def set_age(self, age):
    self.age = age
```

---

## **9. What is a method?**
A function defined inside a class.

**Example:**
```python
def speak(self):
    print("Hello")
```

---

## **10. What is `__init__`?**
The constructor that initializes attributes.

**Example:**
```python
def __init__(self, name):
    self.name = name
```

---

## **11. Abstraction, Encapsulation, Information Hiding**
- **Abstraction** → show essential features  
- **Encapsulation** → bundle data + methods  
- **Information hiding** → use private attributes  

**Example:**
```python
class Bank:
    def __init__(self):
        self.__balance = 0
```

---

## **12. What is a property?**
A property allows attribute‑style access with getter/setter logic.

**Example:**
```python
@property
def age(self):
    return self.__age
```

---

## **13. Attribute vs Property**
| Attribute | Property |
|----------|----------|
| Simple variable | Attribute with logic |
| No validation | Can validate or compute |
| Direct access | Access triggers methods |

---

## **14. Pythonic getters and setters**
Use `@property` instead of `get_x()`.

**Example:**
```python
class Person:
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
```

---

## **15. Dynamically create new attributes**
Python allows adding attributes at runtime.

**Example:**
```python
obj.new_attr = "hello"
```

---

## **16. Bind attributes to objects and classes**
- Instance attribute → belongs to one object  
- Class attribute → shared by all objects  

**Example:**
```python
Dog.legs = 4
dog1.color = "brown"
```

---

## **17. What is `__dict__`?**
A dictionary storing an object’s or class’s attributes.

**Example:**
```python
print(obj.__dict__)
```

---

## **18. How Python finds attributes**
Python uses **attribute lookup order**:

1. Instance `__dict__`
2. Class `__dict__`
3. Parent classes (MRO)

---

## **19. How to use `getattr()`**
Retrieve an attribute by name (string).

**Example:**
```python
getattr(obj, "name")
```

---

## **👤 Contributor**
**Eugenio Martinez**  
Student at **Holberton School**

---

