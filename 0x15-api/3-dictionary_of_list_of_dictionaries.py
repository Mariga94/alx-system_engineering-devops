#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/"
    res = requests.get(url + sys.argv[1]).json()
    url_user = "https://jsonplaceholder.typicode.com/users/"
    res_user = requests.get(url_user).json()
    todos = requests.get(url).json()
    user_id = res_user["id"]
    username = res_user["username"]

    with open('todo_all_employees.json', 'w') as f:
        for todo in todos:
            json.dump({todo.get("userId"): [
                      {"username": todo.get("username"),
                       "task": todo.get("title"),
                       "completed": todo.get("completed"),
                       }]}, f, indent=2)
