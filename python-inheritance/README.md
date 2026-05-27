

---

# 📘 Python Inheritance — Study Guide (Expanded Edition)

## 📚 Overview
This document provides a detailed explanation of **Python inheritance**, including how classes relate to each other, how attributes and methods are shared, and how Python resolves method lookups.  
It also includes **examples of single, multilevel, and multiple inheritance**, along with deeper explanations of **why each type exists** and **how Python decides what to inherit**.

---

# 🧩 Superclass (Base Class / Parent Class)

A **superclass** is a class that provides **common behavior** for other classes to reuse.  
Its purpose is to:

- Define shared attributes  
- Provide default implementations of methods  
- Establish a logical hierarchy  
- Reduce code duplication  

Example:
```python
class Animal:
    def sound(self):
        return "Some sound"
```

A superclass is the **foundation** that subclasses build upon.

---

# 🧩 Subclass (Child Class)

A **subclass** inherits from a superclass and can:

- Extend behavior (add new methods)
- Specialize behavior (override methods)
- Reuse existing logic without rewriting it

Example:
```python
class Dog(Animal):
    pass
```

A subclass represents a **more specific version** of the parent class.

---

# 🔍 Listing All Attributes and Methods

Use `dir()` to inspect:

```python
dir(MyClass)
dir(my_instance)
```

This shows:

- Attributes defined in the class  
- Methods defined in the class  
- Inherited methods  
- Magic methods (`__init__`, `__str__`, etc.)  

This is essential for debugging and understanding inheritance chains.

---

# 🏷️ When Instances Can Have New Attributes

Instances can receive new attributes **dynamically** at runtime:

```python
obj.new_attr = 10
```

This is possible because Python stores instance attributes in a dictionary (`__dict__`), unless the class uses `__slots__`.

This flexibility is part of Python’s dynamic nature.

---

# 🧬 How to Inherit a Class

```python
class Child(Parent):
    pass
```

This creates a **single inheritance** relationship.

---

# 🧬 Multiple Inheritance

```python
class Child(Parent1, Parent2):
    pass
```

Python uses the **Method Resolution Order (MRO)** to determine:

- Which parent class to search first  
- How to resolve conflicts  
- How `super()` behaves  

MRO follows the **C3 linearization algorithm**, ensuring consistent and predictable lookup order.

---

# 🧱 Default Base Class

Every class implicitly inherits from:

```python
object
```

This gives all classes:

- `__str__`
- `__repr__`
- `__eq__`
- `__init__`
- And more

This is why Python is considered a **unified object model**.

---

# ✏️ Overriding Methods or Attributes

To override, simply redefine:

```python
class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    def speak(self):
        print("Child speaking")
```

Overriding allows subclasses to **customize** inherited behavior.

---

# 📥 What Subclasses Inherit

Subclasses inherit:

- Public attributes  
- Public methods  
- Protected members (`_name`)  
- Magic methods unless overridden  

They **do not** inherit:

- Private attributes (`__name`)  
- Constructor arguments unless explicitly called  

Python hides private attributes using **name mangling**, not true privacy.

---

# 🎯 Purpose of Inheritance

Inheritance exists to:

### ✔ **Promote Code Reuse**
Avoid rewriting the same logic in multiple classes.

### ✔ **Create Logical Hierarchies**
Example:  
`Animal → Mammal → Dog`

### ✔ **Enable Polymorphism**
Different subclasses can implement the same method differently.

### ✔ **Improve Maintainability**
Fixing a bug in the superclass fixes it for all subclasses.

### ✔ **Support Extensibility**
New subclasses can be added without modifying existing code.

---

# 🛠️ Built‑in Functions for Inheritance

## `isinstance()`
Checks if an object belongs to a class or its subclasses.

```python
isinstance(obj, MyClass)
```

## `issubclass()`
Checks if one class inherits from another.

```python
issubclass(Child, Parent)
```

## `type()`
Returns the **actual class** of an object.

```python
type(obj)
```

Unlike `isinstance`, `type()` does **not** consider inheritance.

## `super()`
Calls the parent class method following the **MRO**.

```python
super().method()
```

`super()` is essential in multiple inheritance to avoid duplicate calls.

---

# 🧪 Inheritance Examples

---

# 1️⃣ Single Inheritance  
One parent → one child.

### Example 1
```python
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    pass

print(Dog().sound())
```

### Example 2
```python
class Vehicle:
    def move(self):
        return "Moving"

class Car(Vehicle):
    def move(self):
        return "Car driving"

print(Car().move())
```

---

# 2️⃣ Multilevel Inheritance  
Parent → Child → Grandchild.

### Example 1
```python
class A:
    def show(self):
        return "A"

class B(A):
    pass

class C(B):
    pass

print(C().show())
```

### Example 2
```python
class Living:
    def breathe(self):
        return "Breathing"

class Animal(Living):
    pass

class Human(Animal):
    pass

print(Human().breathe())
```

---

# 3️⃣ Multiple Inheritance  
Child inherits from multiple parents.

### Example 1
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
print(d.fly(), d.swim())
```

### Example 2
```python
class A:
    def a(self):
        return "A"

class B:
    def b(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.a(), c.b())
```

---

# 📌 Summary Table

| Concept | Meaning |
|--------|---------|
| Superclass | Parent class |
| Subclass | Child class |
| `dir()` | Lists attributes/methods |
| Dynamic attributes | Added anytime unless using `__slots__` |
| Inheritance syntax | `class Child(Parent)` |
| Multiple inheritance | `class Child(P1, P2)` |
| Default parent | `object` |
| Override | Redefine method in subclass |
| Inherited members | Public + protected |
| Purpose | Reuse, extend, organize |
| `isinstance` | Object → class check |
| `issubclass` | Class → class check |
| `type` | Returns object’s class |
| `super` | Calls parent method |

---

