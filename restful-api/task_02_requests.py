#!/usr/bin/python3

"""Functions to fetch posts from JSONPlaceholder and print/save them."""

import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")


def fetch_and_save_posts():
    """Fetches all posts and saves them into posts.csv."""

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        # Structure data into a list of dictionaries
        structured_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts saved to posts.csv")

    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
