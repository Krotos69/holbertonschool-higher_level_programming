**JavaScript - Warm Up**

---

```markdown
# JavaScript - Warm Up

## Overview
JavaScript is one of the most powerful and widely used programming languages in modern development. It runs natively in all web browsers, powers interactive websites, and extends into backend development through environments like Node.js. This warm‑up guide introduces essential JavaScript concepts such as variables, control flow, loops, functions, and objects. It is designed to give beginners a strong foundation before moving into more advanced topics.

## Introduction
The **JavaScript – Warm Up** module focuses on building core programming skills. You will learn how JavaScript executes code, how to declare variables, how to control program flow, and how to write reusable functions. These fundamentals are essential for any developer working with web technologies.

---

# Full JavaScript Study Guide

## 1. Why JavaScript Programming Is Amazing
JavaScript is the only programming language that runs natively in all web browsers. It enables interactive web pages, dynamic content, and full applications. It is flexible, beginner‑friendly, and used everywhere—from frontend to backend.

---

## 2. How to Run JavaScript
### In HTML
```html
<script>
  console.log("Hello World");
</script>
```

### External File
```html
<script src="script.js"></script>
```

### Browser Console
Open DevTools → Console → type JavaScript.

### Node.js
```bash
node file.js
```

---

## 3. Variables and Constants
Variables store values. JavaScript uses `let`, `const`, and `var`.

### Declaring Variables
```js
let myName;
myName = "Chris";
```

### Declaring Constants
```js
const PI = 3.14;
```
Constants must be initialized and cannot be reassigned.

---

## 4. Differences Between var, let, and const
| Keyword | Scope | Redeclaration | Reassignment | Notes |
|--------|--------|--------------|--------------|-------|
| var | Function | Yes | Yes | Hoisted; avoid in modern JS |
| let | Block | No | Yes | Preferred for mutable values |
| const | Block | No | No | Preferred for fixed values |

---

## 5. JavaScript Data Types
- Number
- String
- Boolean
- Undefined
- Null
- Object
- Array
- Symbol
- BigInt

JavaScript is dynamically typed.

---

## 6. If and If…Else Statements
```js
if (condition) {
  // code
} else {
  // alternative
}
```

Multiple conditions:
```js
if (a > b) {
} else if (a === b) {
} else {
}
```

---

## 7. Comments
```js
// Single-line comment

/*
  Multi-line comment
*/
```

---

## 8. Assigning Values to Variables
```js
let x = 10;
x = 20;
```

---

## 9. Loops: while and for
### while
```js
while (i < 10) {
  i++;
}
```

### for
```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

---

## 10. break and continue
```js
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  if (i % 2 === 0) continue;
}
```

---

## 11. Functions
Functions are reusable blocks of code.

### Declaring
```js
function greet(name) {
  return `Hello ${name}`;
}
```

### Calling
```js
greet("Chris");
```

### Arrow Functions
```js
const add = (a, b) => a + b;
```

---

## 12. What Does a Function Return Without `return`?
It returns `undefined`.

---

## 13. Scope of Variables
- **Global scope**: accessible everywhere
- **Function scope**: inside a function
- **Block scope**: inside `{}` when using `let` or `const`

`var` ignores block scope.

---

## 14. Arithmetic Operators
- `+` addition  
- `-` subtraction  
- `*` multiplication  
- `/` division  
- `%` modulo  
- `**` exponentiation  

Example:
```js
3 + 4 * 5; // 23
```

---

## 15. Manipulating Dictionaries (Objects)
```js
let dog = { name: "Spot", breed: "Dalmatian" };
dog.name;        // access
dog.age = 5;     // add
delete dog.breed; // remove
```

---

## 16. Importing Files (Modules)
### Browser ES Modules
```js
import { myFunc } from "./module.js";
```

### Node.js CommonJS
```js
const fs = require("fs");
```

---

## Installing Node.js 14 (WSL)
1. Update packages:
```bash
sudo apt update
```
2. Install Node.js 14:
```bash
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs
```
3. Verify installation:
```bash
node -v
npm -v
```

---

## Installing semi-standard (WSL)
Semi‑standard is a JavaScript linter.

Install globally:
```bash
npm install --global semi-standard
```

Run it:
```bash
semi-standard
```

---

## Summary
This guide covers all essential JavaScript fundamentals: variables, control flow, functions, objects, loops, and modules. Use it as a foundation for deeper learning.

---

**Author**
*Eugenio martinez*

```
1
---

