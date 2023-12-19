#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)
    name = response.json().get("name")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        argv[1])
    response = requests.get(url)
    tasks = response.json()
    completed = [task for task in tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(name, len(completed),
                                                          len(tasks)))
    for task in completed:
        print("\t {}".format(task.get("title")))
