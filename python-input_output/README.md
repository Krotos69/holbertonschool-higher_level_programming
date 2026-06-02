

---

# 📘 Python - Input/Output — File I/O, JSON, Exceptions & sys

A complete study‑oriented project summarizing essential Python concepts based on the official Python documentation you uploaded.  
This README includes **definitions**, **explanations**, and **code examples** for each topic.

---

# 📝 Table of Contents
1. [Project Description](#project-description)  
2. [Installation](#installation)  
3. [Usage Examples](#usage-examples)  
4. [Python Study Guide](#python-study-guide)  
   - [File I/O](#file-io)  
   - [Reading Files](#reading-files)  
   - [Writing Files](#writing-files)  
   - [Appending to Files](#appending-to-files)  
   - [JSON Serialization](#json-serialization)  
   - [JSON Deserialization](#json-deserialization)  
   - [Exceptions](#exceptions)  
   - [Command‑line Arguments (`sys.argv`)](#command-line-arguments-sysargv)  
5. [Author](#author)

---

# 📘 Project Description
This project demonstrates how Python handles:

- Reading and writing text files  
- Appending to files  
- JSON serialization/deserialization  
- Exception handling  
- Command‑line argument processing  

All explanations are grounded in your uploaded Python documentation.

---

# ⚙️ Installation
```bash
git clone <your-repo-url>
cd <project-folder>
python3 <script>.py
```

---

# 🚀 Usage Examples

### Read a file
```python
read_file("my_file.txt")
```

### Write to a file
```python
write_file("output.txt", "Hello Holberton!\n")
```

### Append to a file
```python
append_write("log.txt", "New entry.\n")
```

### JSON example
```python
import json
json.dumps({"name": "Eugenio"})
```

### Command‑line arguments
```python
import sys
print(sys.argv)
```

---

# 📚 Python Study Guide

Below is the reorganized, logical study guide with definitions and examples.

---

## 📂 File I/O

### 🔹 Definition  
From your uploaded docs:

> “`open(filename, mode, encoding)` returns a file object… mode can be `'r'`, `'w'`, `'a'`…”  
> “It is good practice to use the `with` keyword when dealing with file objects.”

Python uses `open()` to interact with files.  
Modes include:

| Mode | Meaning |
|------|---------|
| `'r'` | Read (default) |
| `'w'` | Write (overwrite) |
| `'a'` | Append |
| `'r+'` | Read & write |

---

## 📖 Reading Files

### 🔹 Definition  
From the docs:

> “`f.read(size)` reads data… `f.readline()` reads a single line… looping over a file is efficient.”

### 🔹 Example
```python
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

## ✍️ Writing Files

### 🔹 Definition  
From the docs:

> “`'w'` for only writing (an existing file with the same name will be erased).”  
> “`f.write(string)` returns the number of characters written.”

### 🔹 Example
```python
with open("output.txt", "w", encoding="utf-8") as f:
    chars = f.write("Hello World!\n")
print(chars)
```

---

## ➕ Appending to Files

### 🔹 Definition  
From the docs:

> “`'a'` opens the file for appending; any data written is added to the end.”

### 🔹 Example
```python
with open("log.txt", "a", encoding="utf-8") as f:
    chars = f.write("New log entry.\n")
print(chars)
```

---

## 🔄 JSON Serialization

### 🔹 Definition  
From the docs:

> “The `json` module can take Python data hierarchies and convert them to string representations; this process is called **serializing**.”

### 🔹 Example
```python
import json

data = {"name": "Eugenio", "age": 25}
json_string = json.dumps(data, indent=4)
print(json_string)
```

---

## 🔁 JSON Deserialization

### 🔹 Definition  
From the docs:

> “Reconstructing the data from the string representation is called **deserializing**.”

### 🔹 Example
```python
import json

json_text = '{"name": "Eugenio", "age": 25}'
data = json.loads(json_text)
print(data["name"])
```

---

## ⚠️ Exceptions

### 🔹 Definition  
From the docs:

> “Errors detected during execution are called **exceptions**.”  
> “The `try` statement works as follows… if an exception occurs, the except clause is executed.”

### 🔹 Example
```python
try:
    number = int("hello")
except ValueError:
    print("Invalid number!")
```

---

## 🖥️ Command‑line Arguments (`sys.argv`)

### 🔹 Definition  
From the docs:

> “`sys.argv` — The list of command line arguments passed to a Python script.”

### 🔹 Example
```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

---

# 👤 Author

**Eugenio Martinez**

---

