#!/usr/bin/python3
'''This Python module is used to gather data from an
API and it returns JSON files'''
import requests
from sys import argv

if __name__ == "__main__":
    employer_id = int(argv[1])
    empl_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employer_id)).json()["name"]
    todo_list = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employer_id)).json()

    tasks = len(todo_list)
    done_with = 0

    for i in todo_list:
        if i["completed"] is True:
            done_with += 1

    print("Employee {} is done with tasks({}/{}):".format(
        empl_name, done_with, tasks))
    for i in todo_list:
        if i["completed"] is True:
            print("\t {}".format(i["title"]))
