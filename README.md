# holbertonschool-higher_level_programming
Python learning course
Learning Python: Overview
 Introduction
Python is one of the most widely used programming languages in the world due to its readability, versatility, and beginner friendly syntax. Whether you're exploring software development, data science, automation, or scripting, Python provides a solid foundation for building real world applications.
This guide introduces essential concepts every beginner should master, focusing on practical skills that help you write clean, efficient, and well structured Python code.
________________________________________
 Learning Objectives
By the end of this learning module, you will understand:
•	How to use the Python interpreter
•	How to print text and variables using print()
•	How to use strings
•	What indexing and slicing are in Python
•	What the official Python coding style is and how to check your code with pycodestyle
________________________________________
 Using the Python Interpreter
The Python interpreter allows you to run Python commands interactively.
How to start it:
•	On Linux/macOS: 
•	python3
•	On Windows: 
•	python
What you can do:
•	Execute Python expressions: 
•	>>> 2 + 3
•	5
•	Test small code snippets quickly
•	Explore functions and objects using: 
•	>>> help()
The interpreter is perfect for experimentation and learning.
________________________________________
 Printing Text and Variables with print()
The print() function displays information to the screen.
Examples:
print("Hello, world!")
Printing variables:
name = "Krotos"
print("Hello,", name)
Formatted printing:
age = 25
print(f"My name is {name} and I am {age} years old.")
________________________________________
 Working with Strings
Strings are sequences of characters enclosed in quotes.
Creating strings:
text = "Python is fun!"
Common operations:
•	Concatenation: 
•	"Hello " + "World"
•	Repetition: 
•	"Hi! " * 3
•	Useful methods: 
•	text.lower()
•	text.upper()
•	text.replace("fun", "powerful")
Strings are essential for handling text, user input, and output formatting.
________________________________________
 Indexing and Slicing
Python treats strings as sequences, allowing you to access parts of them.
Indexing (accessing a single character):
text = "Python"
text[0]   # 'P'
text[-1]  # 'n'
Slicing (extracting a substring):
text[0:3]   # 'Pyt'
text[2:]    # 'thon'
text[:4]    # 'Pyth'
text[::2]   # 'Pto'
Indexing and slicing are powerful tools for manipulating text and sequences.
________________________________________
 Python Coding Style (PEP 8) & pycodestyle
Python follows an official style guide called PEP 8, which promotes clean, readable, and consistent code.
Key PEP 8 rules:
•	Use 4 spaces for indentation
•	Keep lines under 79 characters
•	Use meaningful variable names
•	Add spaces around operators: 
•	x = 5 + 3
Checking your code with pycodestyle:
Install it:
pip install pycodestyle
Run it on a file:
pycodestyle script.py
This tool helps ensure your code follows best practices and remains clean and maintainable.
________________________________________
