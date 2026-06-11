#!/usr/bin/python3
"""
Task 02 - Consuming and processing data from an API using Python.

This module provides two functions:
- fetch_and_print_posts(): Fetches posts and prints status + titles.
- fetch_and_save_posts(): Fetches posts and saves id/title/body to posts.csv.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print:
    - Status code
    - Titles of all posts (if request is successful)
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful, parse JSON and print titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save them into posts.csv.
    CSV columns: id, title, body
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure data into list of dictionaries
        formatted_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)

        print("posts.csv has been created successfully.")
    else:
        print("Failed to fetch posts.")
