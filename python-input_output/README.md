

---

#   Python - input/output File Handling & JSON Guide  


---

##    Project Description
This project is a concise and practical guide that introduces essential Python concepts related to file handling, JSON manipulation, and command‑line argument processing. It serves as a reference for beginners and intermediate learners who want to understand how Python interacts with files and structured data.

---

##    Project Purpose
The purpose of this project is to provide a clear, hands‑on explanation of:

- How Python works with files  
- How to safely read, write, and manage file resources  
- How JSON serialization and deserialization work  
- How to handle command‑line arguments in Python scripts  

It aims to help learners build confidence in writing Python programs that interact with the filesystem and external data.

---

##    Problem Solved
Many new Python developers struggle with:

- Understanding file modes  
- Ensuring files close properly  
- Navigating file cursors  
- Converting data to/from JSON  
- Accessing command‑line parameters  

This guide solves those problems by offering simple explanations and ready‑to‑use examples.

---

##    Commands and Definitions

### **Opening a File**
```python
open("file.txt", "r")
```

### **Writing to a File**
```python
file.write("Hello")
```

### **Reading Entire File**
```python
file.read()
```

### **Reading Line by Line**
```python
for line in file:
    print(line)
```

### **Moving the Cursor**
```python
file.seek(0)
```

### **Ensuring a File Closes**
Use `with` to auto‑close:
```python
with open("file.txt") as f:
    ...
```

### **JSON Serialization**
Convert Python → JSON:
```python
json.dumps(data)
```

### **JSON Deserialization**
Convert JSON → Python:
```python
json.loads(json_string)
```

### **Command‑Line Arguments**
```python
import sys
sys.argv
```

---

##    Usage
Use this guide as a reference while building Python scripts that:

- Read or write files  
- Process structured JSON data  
- Accept input from the command line  

Each section includes examples you can copy directly into your code.

---

##    Command Examples

### Write to a File
```python
with open("notes.txt", "w") as f:
    f.write("Python is awesome!")
```

### Read a File Line by Line
```python
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Convert Python to JSON
```python
import json
data = {"name": "Eugenio", "age": 25}
json_string = json.dumps(data)
```

### Convert JSON to Python
```python
data = json.loads('{"name": "Eugenio"}')
```

### Access Command‑Line Arguments
```python
import sys
print(sys.argv)
```

---

##    How to Implement

1. **Create a Python file**  
   Example: `main.py`

2. **Import necessary modules**  
   ```python
   import json
   import sys
   ```

3. **Use file handling functions**  
   Apply `open()`, `read()`, `write()`, `seek()`, or `with` depending on your task.

4. **Use JSON utilities**  
   - `json.dumps()` for serialization  
   - `json.loads()` for deserialization  

5. **Handle command‑line arguments**  
   Access them through `sys.argv`.

6. **Run your script**  
   ```bash
   python main.py arg1 arg2
   ```


**Author:** *Eugenio Martinez*
---
