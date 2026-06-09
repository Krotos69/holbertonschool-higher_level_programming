

---

# `task_00.md`

# **0. Basics of HTTP/HTTPS**

## **Background**
The **Hypertext Transfer Protocol (HTTP)** defines how clients and servers communicate on the web.  
Its secure version, **HTTPS**, adds encryption using **SSL/TLS**, protecting data from interception, tampering, and impersonation.

---

## **Objective Answers**

---

# **1. Differentiating HTTP and HTTPS**

### **Main Differences**

| Feature | HTTP | HTTPS |
|--------|------|--------|
| **Security** | No encryption; data is sent in plain text | Encrypted using SSL/TLS |
| **Port** | Uses port **80** | Uses port **443** |
| **URL Scheme** | `http://` | `https://` |
| **Data Protection** | Vulnerable to eavesdropping, MITM attacks | Protects confidentiality, integrity, and authenticity |
| **Certificate Requirement** | No certificate needed | Requires an SSL/TLS certificate issued by a CA |
| **Use Cases** | Non‑sensitive content | Login pages, payments, APIs, any sensitive data |

### **Security Focus**
- HTTPS encrypts the communication channel, preventing attackers from reading or modifying data.  
- It authenticates the server using certificates.  
- It ensures integrity: data cannot be altered without detection.

### **Optional Observation (Wireshark)**
- **HTTP traffic** appears in plain text (you can read headers and body).  
- **HTTPS traffic** appears encrypted; you cannot read the content.

---

# **2. Understanding HTTP Structure**

After inspecting a webpage using the browser’s **Network** tab, a typical HTTP request/response structure looks like this:

### **HTTP Request Structure**
- **Method:** e.g., `GET`, `POST`  
- **URL/Path:** e.g., `/index.html`  
- **Protocol Version:** `HTTP/1.1`, `HTTP/2`  
- **Request Headers:**  
  - `Host`  
  - `User-Agent`  
  - `Accept`  
  - `Content-Type` (for POST/PUT)  
- **Request Body:**  
  - Only present in methods like POST/PUT  
  - Contains form data, JSON, etc.

### **HTTP Response Structure**
- **Status Line:**  
  - Example: `HTTP/1.1 200 OK`
- **Response Headers:**  
  - `Content-Type`  
  - `Content-Length`  
  - `Server`  
  - `Date`
- **Response Body:**  
  - HTML, JSON, images, etc.

### **Example Observation**
When loading a webpage, the first request is usually:
- Method: **GET**  
- Status: **200 OK**  
- Response headers show server type, content type, and caching rules.

---

# **3. Exploring HTTP Methods and Status Codes**

## **A. Common HTTP Methods (with explanations)**

- **GET**  
  Retrieves data from the server.  
  *Example:* Loading a webpage or fetching API data.

- **POST**  
  Sends data to the server to create a new resource.  
  *Example:* Submitting a login form or creating a new user in an API.

- **PUT**  
  Updates an existing resource by replacing it entirely.  
  *Example:* Updating a user profile in an API.

- **DELETE**  
  Removes a resource from the server.  
  *Example:* Deleting a record from a database via an API endpoint.

---

## **B. Common HTTP Status Codes (with scenarios)**

- **200 OK**  
  The request was successful.  
  *Scenario:* A webpage loads normally.

- **301 Moved Permanently**  
  The resource has a new URL.  
  *Scenario:* A website redirects from `http://` to `https://`.

- **400 Bad Request**  
  The server cannot process the request due to malformed syntax.  
  *Scenario:* Sending invalid JSON in a POST request.

- **404 Not Found**  
  The requested resource does not exist.  
  *Scenario:* Visiting a broken or outdated link.

- **500 Internal Server Error**  
  The server encountered an unexpected condition.  
  *Scenario:* A backend bug or misconfiguration causes the server to crash.

---

   **Author :**
   Eugenio Martinez.