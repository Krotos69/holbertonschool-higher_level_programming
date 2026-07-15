
---

# JavaScript DOM Manipulation  
## Overview  
Structured study guide covering essential DOM manipulation techniques in JavaScript. It includes element selection, styling, content updates, DOM modification, network requests, and event handling. All sections are aligned with Holberton’s learning style: clear explanations, practical examples, and MDN‑backed concepts.

---

## Selecting HTML Elements  
**Definition:**  
Selecting elements means retrieving specific nodes from the DOM so JavaScript can read, modify, or interact with them. The DOM exposes multiple methods to target elements by CSS selectors, IDs, classes, or tag names.

### **Selectors**
- **`document.querySelector(selector)`** — first matching element  
- **`document.querySelectorAll(selector)`** — all matching elements  
- **`document.getElementById(id)`** — unique ID lookup  
- **`document.getElementsByClassName(class)`** — live HTMLCollection  
- **`document.getElementsByTagName(tag)`** — all elements with a tag  

### Example
```js
const title = document.querySelector('h1');
const items = document.querySelectorAll('.item');
```

---

## Differences Between ID, Class, and Tag Selectors  
**Definition:**  
Selectors define how you target elements in the DOM. Each selector type has a specific purpose: IDs for unique elements, classes for groups, and tags for broad structural selection.

### **ID Selector (`#id`)**
- Must be unique  
- Fastest lookup  
- Used for single, specific elements  

### **Class Selector (`.class`)**
- Can be shared  
- Ideal for grouping similar elements  

### **Tag Selector (`tag`)**
- Selects elements by HTML tag  
- Useful for broad selection  

---

## Modifying Element Styles  
**Definition:**  
JavaScript can change how elements look by editing inline styles or manipulating CSS classes. This allows dynamic UI changes such as animations, color changes, or visibility toggles.

### **Inline Style**
```js
const box = document.querySelector('.box');
box.style.backgroundColor = 'blue';
box.style.fontSize = '20px';
```

### **Class Manipulation**
```js
box.classList.add('highlight');
box.classList.remove('hidden');
```

---

## Getting & Updating Element Content  
**Definition:**  
Content manipulation allows JavaScript to read or modify the text or HTML inside an element. This is essential for dynamic interfaces, form updates, and rendering data.

### **Read Content**
```js
element.textContent;
element.innerHTML;
```

### **Update Content**
```js
element.textContent = 'New text';
element.innerHTML = '<strong>Bold text</strong>';
```

---

## Modifying the DOM  
**Definition:**  
DOM modification refers to creating, inserting, removing, or replacing nodes in the document structure. This is how JavaScript builds dynamic interfaces, adds elements, or updates layouts.

### **Create Elements**
```js
const p = document.createElement('p');
p.textContent = 'Hello!';
```

### **Insert Elements**
```js
document.body.appendChild(p);
```

### **Remove Elements**
```js
p.remove();
```

### **Replace Elements**
```js
oldNode.replaceWith(newNode);
```

---

## Making Requests with XMLHttpRequest  
**Definition:**  
`XMLHttpRequest` (XHR) is an older API used to send HTTP requests from JavaScript. It supports asynchronous communication but is more verbose compared to modern alternatives.

```js
const request = new XMLHttpRequest();
request.open('GET', 'data.json');
request.responseType = 'json';

request.onload = () => {
  console.log(request.response);
};

request.onerror = () => console.error('XHR error');
request.send();
```

---

## Making Requests with Fetch API  
**Definition:**  
The Fetch API is a modern, promise‑based interface for making HTTP requests. It is cleaner, easier to use, and supports async/await, making it the preferred method for network operations.

```js
fetch('data.json')
  .then(response => {
    if (!response.ok) throw new Error(response.status);
    return response.json();
  })
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

---

## Listening to DOM Events  
**Definition:**  
DOM events notify JavaScript when something happens in the document (e.g., page loaded, element changed). Event listeners allow your code to react to these changes.

### **Basic Pattern**
```js
button.addEventListener('click', () => {
  console.log('Button clicked');
});
```

### **Common Events**
- `DOMContentLoaded`  
- `scroll`  
- `input`  
- `change`  
- `focus` / `blur`  

---

## Listening to User Events  
**Definition:**  
User events are interactions performed by the user, such as mouse movements, keyboard presses, or touch gestures. JavaScript listens to these events to create interactive experiences.

### **Mouse Events**
```js
element.addEventListener('mouseover', handler);
element.addEventListener('mousedown', handler);
element.addEventListener('mouseup', handler);
```

### **Keyboard Events**
```js
document.addEventListener('keydown', e => {
  console.log(e.key);
});
```

### **Touch Events**
```js
element.addEventListener('touchstart', handler);
```

---

## Author 
- **Eugenio Martinez, Holberton School Student**

---

