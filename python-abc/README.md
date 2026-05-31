
---

# **Python OOP — Abstract Classes, Interfaces, and Subclassing**

## **Overview**
This repository contains a curated set of exercises designed to strengthen your understanding of **Object‑Oriented Programming (OOP)** in Python.  
You will work with **abstract classes**, **interfaces**, **duck typing**, **method overriding**, **mixins**, and **subclassing Python’s built‑in types**.

These exercises are intentionally hands‑on: you will design classes, enforce contracts, extend built‑ins, and test polymorphic behavior across multiple OOP patterns.

---

## **📌 Learning Objectives**

## 1. **Abstract Classes**  

Abstract classes define a **shared interface** for subclasses and prevent direct instantiation.  
They are created using Python’s `abc` module and allow you to enforce that all subclasses implement specific methods.

### **Why Use Abstract Classes**
- Enforce required methods across subclasses  
- Prevent incomplete implementations  
- Provide shared logic while still requiring subclass customization  

### **Example**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # 78.5
```

---

## 2. **Interfaces and Duck Typing**  


Python does not have formal interfaces like Java or C#.  
Instead, it uses **duck typing**, meaning that if an object has the required behavior, it is acceptable — regardless of its class.

### **Why Use Duck Typing**
- More flexible and Pythonic  
- Reduces unnecessary inheritance  
- Encourages behavior‑based design  

### **Example**
```python
class JSONExporter:
    def export(self, data):
        return f"Exporting {data} to JSON"

class XMLExporter:
    def export(self, data):
        return f"Exporting {data} to XML"

def save(data, exporter):
    # Duck typing: only requires exporter.export()
    print(exporter.export(data))

save({"name": "Alice"}, JSONExporter())
save({"name": "Alice"}, XMLExporter())
```

---

## 3. **Subclassing Standard Base Classes**  


Python allows you to extend built‑in types such as `list`, `dict`, and `Iterator`.  
This is useful when you want custom behavior while keeping familiar interfaces.

### **Why Subclass Built‑ins**
- Add validation  
- Track operations  
- Create domain‑specific data structures  

### **Example: Custom List**
```python
class PositiveList(list):
    def append(self, value):
        if value < 0:
            raise ValueError("Only positive numbers allowed")
        super().append(value)

nums = PositiveList()
nums.append(10)
nums.append(-5)  # Raises ValueError
```

### **Example: Custom Iterator**
```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(3):
    print(n)
```

---

## 4. **Method Overriding**  


Method overriding allows a subclass to **replace or extend** a method inherited from a parent class.

### **Why Override Methods**
- Customize inherited behavior  
- Extend base functionality  
- Implement polymorphism  

### **Example**
```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # Polymorphism
```

---

## 5. **Multiple Inheritance**  


Python allows a class to inherit from **multiple parent classes**, enabling powerful composition of behaviors.

### **Why Use Multiple Inheritance**
- Combine behaviors from multiple sources  
- Create flexible class hierarchies  
- Implement mixins (next section)  

### **Example**
```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
print(d.fly())   # Flying
print(d.swim())  # Swimming
```

---

## 6. **Mixins**  


Mixins are small, reusable classes that provide **specific behavior**.  
They are not meant to stand alone — they are designed to be combined with other classes.

### **Why Use Mixins**
- Avoid deep inheritance chains  
- Compose behavior cleanly  
- Reuse logic across unrelated classes  

### **Example**
```python
class LogMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Worker(LogMixin):
    def do_work(self):
        self.log("Work started")
        # ... work ...
        self.log("Work finished")

w = Worker()
w.do_work()
```

---

## **📚 Recommended Resources**

These official and community resources support the concepts covered in the exercises:

- **Python Docs — Classes**  
  [https://docs.python.org/3/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)

- **Python Docs — `abc` Abstract Base Classes**  
  [https://docs.python.org/3/library/abc.html](https://docs.python.org/3/library/abc.html)

- **Real Python — OOP in Python 3**  
  [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)

- **YouTube Playlist — Python OOP Tutorials**  
  [https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G)

---

## **🧩 What You Will Build**
Throughout the exercises, you will create:

- Abstract shapes with enforced geometric methods  
- Interface‑like protocols for data processing  
- Custom collections by subclassing `list` and `dict`  
- Iterator and generator‑based classes  
- Mixins for logging, serialization, and validation  
- Multiple‑inheritance class hierarchies  
- Polymorphic systems demonstrating duck typing

Each exercise builds on the previous one, gradually increasing complexity.

---

## **🛠️ Technologies Used**
- Python 3.10+  
- `abc` module  
- Built‑in data structures  
- Type hints (`typing` module)  
- Unit testing (optional but encouraged)

---

## **🚀 Getting Started**

### **1. Clone the repository**
```bash
git clone <your-repo-url>
cd python-oop-exercises
```

### **2. Run the exercises**
Each exercise is located in its own directory with instructions and starter code.

### **3. Run tests (optional)**
```bash
pytest
```

---

## **📁 Repository Structure**
```
python-oop-exercises/
│
├── 01_abstract_classes/
├── 02_interfaces_duck_typing/
├── 03_subclassing_builtins/
├── 04_method_overriding/
├── 05_multiple_inheritance/
├── 06_mixins/
└── README.md
```

---

## **💡 Autor **
    Eugenio Martinez

---

