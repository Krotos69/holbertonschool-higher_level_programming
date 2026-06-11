

---

# `task_01.md`

# **1. Consume Data from an API Using Command‑Line Tools (curl)**

## **Background**
`curl` (Client URL) is a command‑line tool used to transfer data to or from a server using protocols such as **HTTP**, **HTTPS**, **FTP**, and more.  
It is widely used for:

- Testing and debugging APIs  
- Sending HTTP requests  
- Inspecting responses  
- Automating API interactions  

Mastering `curl` allows developers to interact with REST APIs directly from the terminal.

---

## **Objective**

---

# **1. Installing and Basic Interaction with curl**

### **Installing curl**
- On **Linux** (Debian/Ubuntu):  
  ```bash
  sudo apt install curl
  ```
- On **macOS** (usually preinstalled):  
  ```bash
  curl --version
  ```
- On **Windows**, use:
  - **WSL** (recommended), or  
  - Download curl from the official curl website.

### **Confirm Installation**
Running:
```bash
curl --version
```
Produces output similar to:
```
curl 8.x.x (x86_64-pc-linux-gnu) libcurl/8.x.x OpenSSL/3.x
```
This confirms curl is installed and ready.

### **Fetching a Webpage**
Command:
```bash
curl http://example.com
```

### **Explanation**
- `curl` sends a **GET request** to the URL.
- The server responds with the **HTML content** of the page.
- The terminal displays the raw HTML.

This demonstrates the most basic use of curl: retrieving web content.

---

# **2. Fetching Data from an API**

### **Retrieve Posts from JSONPlaceholder**
Command:
```bash
curl https://jsonplaceholder.typicode.com/posts
```

### **What Happens**
- curl sends a **GET request** to the `/posts` endpoint.
- The server returns a **JSON array** of 100 posts.

### **Example of the output (truncated)**
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati",
    "body": "quia et suscipit..."
  },
  ...
]
```

### **Interpretation**
- The API returns structured JSON data.
- Each object represents a post with fields like `userId`, `id`, `title`, and `body`.
- This demonstrates how curl interacts with REST APIs.

---

# **3. Using Headers and Other Options with curl**

## **A. Fetch Only the Headers**
Command:
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

### **Explanation**
- `-I` (uppercase i) means **HEAD request**.
- It retrieves **only the response headers**, not the body.

### **Example Output**
```
HTTP/2 200
date: Thu, 11 Jun 2026 16:00:00 GMT
content-type: application/json; charset=utf-8
x-powered-by: Express
```

### **Interpretation**
- Shows the **status code**, **content type**, **server**, and other metadata.
- Useful for debugging caching, content type, and server behavior.

---

## **B. Making a POST Request**
Command:
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

### **Explanation**
- `-X POST` → sets the HTTP method to POST  
- `-d` → sends form‑encoded data in the request body  
- The API receives the data and creates a new resource (simulated)

### **Example Response**
```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

### **Interpretation**
- JSONPlaceholder simulates creation and returns the new object.
- The `id` is always **101** because the API is fake and does not store data.
- This demonstrates how to send data to an API using curl.

---

### **Author** : **Eugenio Martinez** 