#!/usr/bin/python3
"""Module with a python script"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    empl_id = int(argv[1])
    empl = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                empl_id)).json()
    empl_username = empl["username"]
    todo_list = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                empl_id)).json()

    with open("{}.csv".format(empl_id), "w", newline="") as csvfile:
        for i in todo_list:
            var_list = [empl_id, empl_username, i["completed"], i["title"]]
            csvwriter = csv.writer(
                    csvfile, delimiter=',',
                    quotechar='"', quoting=csv.QUOTE_ALL)
            csvwriter.writerow(var_list)
