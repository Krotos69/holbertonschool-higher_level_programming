#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = {}

@app.route("/")  # Route for the root URL
def home():
    return "Welcome to the Flask API!"

@app.route("/status")    # Route for checking the status of the API
def status():
    return "OK"

@app.route("/data")    # Route for getting the list of users
def get_data():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")    # Route for getting user details by username
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])    # Route for adding a new user with POST method
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

# Store full user details in the users dictionary, using the username as the key
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

# Important: return ONLY the user object
    return jsonify(users[username]), 201

if __name__ == "__main__":
    app.run()    # Run the Flask application on the default port (5000)
