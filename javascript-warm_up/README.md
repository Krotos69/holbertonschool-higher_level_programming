  

---

# JavaScript - Warm-Up

## 📘 Project Overview
This project introduces the essential foundations of **JavaScript** for scripting and basic front‑end development.  
You will learn how JavaScript runs, how variables behave, how to use control flow, how functions work, and how to manipulate objects.  
These concepts form the backbone of all modern JavaScript programming, whether in the browser or in Node.js.

---

---

## ⭐ Why is JavaScript programming amazing?
JavaScript is one of the most versatile languages in the world. It runs in every browser, powers interactive websites, and can also run on servers using Node.js. Its flexibility, speed, and massive ecosystem make it essential for modern software engineering.

**Example:**
```js
console.log("JavaScript runs everywhere!");
```

---

## ▶️ How do you run a JavaScript script?
You can run JavaScript in two main environments:

- **Browser:** using a `<script>` tag  
- **Node.js:** running `.js` files directly from the terminal

**Example (Node.js):**
```bash
node script.js
```

---

## 📦 How do you create variables and constants?
JavaScript provides three keywords for storing values:

- `let` → variable that can change  
- `const` → constant that cannot change  
- `var` → older variable keyword (avoid in modern code)

**Example:**
```js
let age = 20;
const pi = 3.14;
```

---

## 🔍 Differences between `var`, `let`, and `const`
- `var` has **function scope** and allows redeclaration  
- `let` has **block scope** and cannot be redeclared  
- `const` has **block scope** and cannot be reassigned or redeclared  

**Example:**
```js
let x = 5;
x = 10; // valid
```

---

## 🧪 What data types exist in JavaScript?
JavaScript has **primitive** and **non‑primitive** types.

**Primitive:**  
`string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint`

**Non‑primitive:**  
`object` (arrays, functions, dictionaries)

**Example:**
```js
let name = "Ana"; // string
```

---

## 🔀 How do you use `if` and `if...else` statements?
Conditionals allow your program to make decisions based on logic.

**Example:**
```js
if (age >= 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

---

## 💬 How do you use comments?
Comments help explain code and are ignored by the interpreter.

**Example:**
```js
// This is a single-line comment
```

---

## 🎯 How do you assign values to variables?
You assign values using the `=` operator. You can also update values using shorthand operators.

**Example:**
```js
let x = 10;
x += 5;
```

---

## 🔁 How do you use `while` and `for` loops?

**while loop:**
```js
let i = 0;
while (i < 3) {
  console.log(i);
  i++;
}
```

**for loop:**
```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

---

## 🛑 How do `break` and `continue` work?
- `break` → stops the loop  
- `continue` → skips the current iteration  

**Example:**
```js
for (let i = 0; i < 5; i++) {
  if (i === 3) break;
  console.log(i);
}
```

---

## 🧰 What is a function and how do you use it?
A function is a reusable block of code that performs a task.

**Example:**
```js
function greet(name) {
  return "Hello " + name;
}
```

---

## ❓ What does a function return if no `return` is used?
It returns `undefined`.

**Example:**
```js
function test() {}
console.log(test()); // undefined
```

---

## 🌐 What is the scope of variables?
Scope determines where a variable can be accessed.

- **Global scope**  
- **Function scope**  
- **Block scope** (`let`, `const`)

**Example:**
```js
if (true) {
  let x = 10; // block-scoped
}
```

---

## ➕ What are the arithmetic operators?
JavaScript supports:

`+`, `-`, `*`, `/`, `%`, `**`

**Example:**
```js
let total = (5 + 3) * 2;
```

---

## 📚 How do you manipulate a dictionary (object)?
Objects store key‑value pairs and can be modified dynamically.

**Example:**
```js
let user = { name: "Ana", age: 22 };
user.age = 23;
```

---

## 📥 How do you import a file?
JavaScript supports two module systems:

**ES Modules:**
```js
import { myFunction } from "./utils.js";
```

**CommonJS:**
```js
const utils = require("./utils.js");
```

---

# 🎯 Learning Objectives
By the end of this warm‑up, you should be able to:

- Explain why JavaScript is widely used  
- Run JavaScript in both browser and Node.js environments  
- Use `var`, `let`, and `const` correctly  
- Identify all JavaScript data types  
- Write conditionals, loops, and functions  
- Understand scope and variable behavior  
- Manipulate objects (dictionaries)  
- Import modules in JavaScript  

---

# 📚 Resources
- MDN Web Docs – JavaScript Guide  
- Node.js Documentation  
- W3Schools JavaScript Basics  
- Holberton School Foundations Curriculum  

---

# ✍️ Author
**Eugenio Martínez**

---
