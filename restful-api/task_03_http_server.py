#!/usr/bin/env python3
"""
Simple HTTP server using Python's http.server module.

This script demonstrates:
- Handling GET requests
- Serving plain text and JSON responses
- Routing based on request path
- Returning proper HTTP status codes
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom request handler for a simple API.
    """

    def do_GET(self):
        """
        Handle GET requests and route based on the request path.
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Endpoint not found
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint does not exist")


def run_server():
    """
    Start the HTTP server on port 8000.
    """
    port = 8000
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
