

---

# **HTTP & HTTPS — Task 0**

## **0. Basics of HTTP/HTTPS**

### **I. HTTP vs HTTPS: Key Security Differences**

---

### **1. Encryption**
- **HTTP**
  - No encryption.
  - Data travels in plain text, exposing usernames, passwords, cookies, etc.
- **HTTPS**
  - Uses **TLS (Transport Layer Security)** to encrypt all data.
  - Intercepted data is unreadable without decryption keys.

---

### **2. Data Integrity**
- **HTTP**
  - Data can be modified in transit without detection.
  - Vulnerable to content injection and MITM attacks.
- **HTTPS**
  - TLS ensures integrity — tampering is detectable.
  - Protects against injection attacks.

---

### **3. Authentication**
- **HTTP**
  - No server identity verification.
  - Easy to spoof malicious sites.
- **HTTPS**
  - Uses **digital certificates** issued by trusted CAs.
  - Confirms the server is legitimate.

---

### **4. Protection Against Common Attacks**

| Attack Type | HTTP | HTTPS |
|------------|------|--------|
| Man‑in‑the‑Middle (MITM) | Vulnerable | Strong protection (encryption + authentication) |
| Eavesdropping | Fully exposed | Encrypted |
| Content Injection | Easy | Blocked by integrity checks |
| Phishing | Easier to spoof | Harder due to certificate validation |

---

### **5. Browser Indicators**
- **HTTP**
  - “Not Secure” warnings.
  - Some features blocked by modern browsers.
- **HTTPS**
  - Padlock icon.
  - Required for modern APIs (geolocation, service workers, etc.).

---

### **6. Performance**
- Old myth: HTTPS is slower.
- Reality:
  - Modern TLS is optimized.
  - Often faster thanks to **HTTP/2** and better connection handling.

---

### **7. SEO and Trust**
- **HTTP**
  - Lower search ranking.
  - Users may distrust the site.
- **HTTPS**
  - Preferred by search engines.
  - Builds user confidence.

---

## **II. Understanding HTTP Structure**

### **HTTP Example**
- http://www.edu4java.com/es/web/web30.html

### **HTTPS Example**
- https://www.w3schools.com/nodejs/nodejs_rest_api.asp

---

## **III. Exploring HTTP Methods and Status Codes**

Understanding HTTP is like understanding the grammar of the web:  
**Methods = verbs**  
**Status codes = server feedback**

---

## **🚀 HTTP Methods (The Web’s Verbs)**

| Method | Purpose | Typical Use Case |
|--------|----------|------------------|
| **GET** | Retrieve a resource | Load a webpage, fetch data |
| **POST** | Create a new resource | Submit forms, create users |
| **PUT** | Replace an existing resource | Update an entire object |
| **PATCH** | Partially update a resource | Update a single field |
| **DELETE** | Remove a resource | Delete a record |
| **HEAD** | GET without body | Check metadata |
| **OPTIONS** | Discover supported methods | CORS preflight |

---

## **📡 HTTP Status Codes (Server Feedback)**

### **Status Code Categories**

| Class | Meaning | Example Codes |
|--------|----------|----------------|
| **1xx** | Informational | 100, 101 |
| **2xx** | Success | 200, 201, 204 |
| **3xx** | Redirection | 301, 302, 304 |
| **4xx** | Client errors | 400, 401, 404 |
| **5xx** | Server errors | 500, 502, 503 |

---

## **⭐ Common Status Codes**

### **200 OK**
Request succeeded; response depends on method.

### **201 Created**
A new resource was created (common after POST).

### **301 Moved Permanently**
Resource has a new permanent URL.

### **302 Found**
Temporary redirect.

### **304 Not Modified**
Use cached version.

### **400 Bad Request**
Malformed request.

### **404 Not Found**
Resource doesn’t exist.

### **500 Internal Server Error**
Generic server failure.

---

## **Why This Matters for Developers**

- Understanding **methods** helps you design clean, predictable APIs.
- Understanding **status codes** helps you debug faster and build resilient clients.

---
