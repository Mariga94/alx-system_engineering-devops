#!/usr/bin/python3
"""
Exports to csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    url_users = "https://jsonplaceholder.typicode.com/users/"
    res_todo = requests.get(url_todo + sys.argv[1])
    json_todo = res_todo.json()

    res_user = requests.get(url_users + sys.argv[1])
    json_user = res_user.json()
    username = json_user["username"]

    todos = requests.get(url_todo).json()
    employee_record = []
    for todo in todos:
        if (todo["userId"] == int(sys.argv[1])):
            employee_record.append("'{}','{}','{}','{}'\n"
                                   .format(todo["userId"],
                                           username,
                                           todo["completed"],
                                           todo["title"]))

    with open('2.csv', 'w', encoding='UTF8') as employee_file:
        employee_writer = csv.writer(employee_file)
        employee_writer.writerow(employee_record)
