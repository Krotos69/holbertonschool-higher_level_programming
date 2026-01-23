________________________________________
 Python: Lists, Tuples, and Sequences
📝 Description
This repository contains a complete guide to the fundamental data structures in Python: lists, tuples, and sequences. It includes detailed explanations, practical examples, comparisons, common use cases, and essential concepts such as list comprehensions, tuple packing, sequence unpacking, and the use of the del statement.
________________________________________
🎯 Purpose
The main goal is to provide a clear and accessible resource for students who want to master basic Python data structures, especially in the context of learning programming fundamentals and preparing for more advanced projects.
________________________________________
❗ Problem
Many students struggle to understand:
•	The difference between lists and tuples
•	When to use each one
•	How to manipulate lists efficiently
•	How sequences work in Python
•	How to apply list comprehensions correctly
•	What packing and unpacking mean
•	How to use the del statement safely
This repository solves those issues with clear explanations and practical examples.
________________________________________
🌍 Context
This content is part of the study of Python - Data Structures: Lists, Tuples, a fundamental topic in educational programs such as Holberton School and introductory programming courses.
Understanding these structures is essential for:
•	Data manipulation
•	Algorithm development
•	Object-oriented programming
•	More advanced structures like dictionaries, sets, and classes
________________________________________
🛠 Installation
No additional installation is required.
You only need Python 3.x installed on your system.
Check your version with:
python3 --version
________________________________________
🚀 Usage
📌 1. Lists: what they are and how to use them
•	Mutable, ordered collections
•	Can store any data type
•	Support indexing, slicing, and modification methods
Example:
numbers = [1, 2, 3]
numbers.append(4)
numbers[1] = 20
________________________________________
📌 2. Differences and similarities between strings and lists
Feature	Lists	Strings
Mutable	✔	✘
Indexable	✔	✔
Iterable	✔	✔
Multiple data types	✔	✘
________________________________________
📌 3. Common list methods
append(), insert(), extend()
remove(), pop(), clear()
index(), count()
sort(), reverse()
________________________________________
📌 4. Lists as stacks (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.pop()
________________________________________
📌 5. Lists as queues (FIFO)
queue = [1, 2, 3]
queue.append(4)
queue.pop(0)
________________________________________
📌 6. List comprehensions
squares = [x*x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
________________________________________
📌 7. Tuples: what they are and how to use them
•	Immutable sequences
•	Faster than lists
•	Useful for constant data
t = (1, 2, 3)
________________________________________
📌 8. When to use tuples vs lists
Use lists when you need to modify data.
Use tuples when the data must remain constant or when you need dictionary keys.
________________________________________
📌 9. What is a sequence
Any ordered collection that supports:
•	Indexing
•	Slicing
•	Iteration
•	len()
Examples: list, tuple, str, range.
________________________________________
📌 10. Tuple packing
t = 1, 2, 3
________________________________________
📌 11. Sequence unpacking
a, b, c = (1, 2, 3)
a, *middle, c = [1, 2, 3, 4, 5]
________________________________________
📌 12. The del statement
x = 10
del x

lst = [1, 2, 3]
del lst[1]
del lst[0:2]
________________________________________
🤝 Author
Eugenio Martinez
