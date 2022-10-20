#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    res = requests.get(url + sys.argv[1]).json()
    url_user = "https://jsonplaceholder.typicode.com/users/"
    res_user = requests.get(url_user + sys.argv[1]).json()
    todos = requests.get(url).json()
    user_id = res_user["id"]
    username = res_user["username"]

    with open('data.json', 'w') as f:
        for todo in todos:
            json.dump({user_id: [
                      {"task": todo.get("title"),
                       "completed": todo.get("completed"),
                       "username": username}]}, f, indent=4)
