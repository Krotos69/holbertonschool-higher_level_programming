

---

# **Python OOP - Abtract Class, Interface, Subclassing**

## **Project Description**

### **Project Purpose**
This project serves as a comprehensive exploration of advanced object‑oriented programming (OOP) concepts in Python. It provides practical examples and implementations that demonstrate how to design flexible, maintainable, and extensible software architectures.

### **Problem Solved**
Modern software systems often require reusable components, consistent interfaces, and predictable behavior across different modules. This project addresses these needs by showcasing patterns and techniques that improve code organization, reduce duplication, and promote clean design.

### **General Context**
The repository is intended for learners, educators, and developers who want to deepen their understanding of OOP beyond the basics. It focuses on real‑world use cases where abstract classes, interfaces, mixins, and inheritance patterns significantly enhance code quality.

---

## **Definition of Topics**

### **Abstract Classes**
- **Definition:** Classes that cannot be instantiated and are meant to define a common interface for subclasses. Implemented using `abc.ABC` and `@abstractmethod`.
- **What it Solves:** Ensures that all subclasses implement required methods, enforcing consistency across related classes.

### **Interfaces & Duck Typing**
- **Definition:** Interfaces define a contract for behavior without dictating implementation. Duck typing relies on an object’s behavior rather than its type.
- **What it Solves:** Promotes flexible code that works with any object that “quacks like a duck,” reducing tight coupling.

### **Subclassing Standard Base Classes**
- **Definition:** Extending built‑in types like `list`, `dict`, or iterators to create specialized data structures.
- **What it Solves:** Allows developers to enhance or modify built‑in behaviors while maintaining compatibility with Python’s ecosystem.

### **Method Overriding**
- **Definition:** Redefining a method in a subclass to change or extend the behavior of its parent class.
- **What it Solves:** Enables customization of inherited functionality without rewriting entire classes.

### **Multiple Inheritance**
- **Definition:** A class inheriting from more than one parent class.
- **What it Solves:** Allows composition of complex behaviors, though it must be used carefully to avoid ambiguity (e.g., diamond problem).

### **Mixins**
- **Definition:** Lightweight classes that provide reusable methods without representing standalone entities.
- **What it Solves:** Encourages code reuse across unrelated classes without forcing deep inheritance hierarchies.

---

## **Use**

### **Command Examples**
```bash
# Run main demonstration script
python main.py

# Execute individual topic demos
python examples/abstract_classes.py
python examples/interfaces.py
python examples/mixins.py
```

### **Screenshots or Demonstrations**
*(Add your images or GIFs here once available)*

### **Basic Use Cases**
- Enforcing method implementation using abstract classes  
- Creating custom containers by subclassing `list` or `dict`  
- Combining behaviors using mixins  
- Demonstrating duck typing through interchangeable objects  
- Overriding methods to extend base functionality  
- Building classes with multiple inheritance to model complex relationships  

---

## **Contribution**

### **Contribution Rules**
- Follow the coding standards outlined below  
- Write clear commit messages  
- Open an issue before submitting major changes  
- Include tests for new features  

### **Workflow with Branches**
- `main` → stable, production‑ready code  
- `dev` → active development  
- Feature branches follow the pattern:  
  ```
  feature/<topic-name>
  fix/<issue-number>
  ```

### **Coding Standards**
- Use PEP 8 style guidelines  
- Prefer composition over deep inheritance when possible  
- Document public classes and methods  
- Write meaningful docstrings and type hints  

---

## **License**

### **License Type**
none

### **Permissions and Restrictions**
- ✔ Free to use, modify, and distribute  
- ✔ Commercial use allowed  
- ✖ No liability or warranty provided  

---

## **Credits / Authors**
**Eugenio Martínez**

---

