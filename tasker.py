#!/usr/bin/env python3

import sys
import os
import sys
import datetime
import json


data_path = os.path.dirname(__file__) + "/data.json"

def initiate_db():
    if not os.path.exists(data_path):
        with open(data_path, "w") as file:
            json.dump([], file)

def get_status():
    try:
        return sys.argv[2]
    except IndexError:
        return "all"

def get_current_time():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def load():
    with open(data_path, "r")as file:
        data = json.load(file)

    return data

def save(data):
    with open(data_path, "w") as file:
        json.dump(data, file, indent=4)

def get_id():
    list_of_ids = []
    current_data = load()

    for task in current_data:
        list_of_ids.append(task["id"])

    for i in range(1, 101):
        if i not in list_of_ids:
            return i
            break

def desc_limit(input):
    space_num = 30 - len(input)
    return input + (space_num*" ")

def add(desc):
    current_data = load()

    if len(current_data) == 100:
        print("Database is full, please remove some task.")

    else:
        data = {}
        data["id"] = get_id()
        data["description"] = desc
        data["status"] = "todo"
        data["created_at"] = get_current_time()
        data["updated_at"] = get_current_time()
        current_data.append(data)
        save(current_data)

def update(id, desc):
    current_data = load()

    try:
        for task in current_data:
            if task["id"] == id:
                task["description"] = desc
                task["updated_at"] = get_current_time()
                break

        save(current_data)

    except IndexError:
        print("No such file is found.")

def delete(id):
    current_data = load()

    try:
        for task in current_data:
            if task["id"] == id:
                current_data.remove(task)

        save(current_data)

    except IndexError:
        print("No such file is found.")

def mark(id, stat):
    stat = stat[1].lower()
    current_data = load()

    for task in current_data:
        if task["id"] == id:
            match stat:
                case "done": task["status"] = "done"
                case "in": task["status"] = "in-progress"
                case _: print("invalid status.")

    save(current_data)

def task_list(status):
    current_data = load()

    index = "ID"
    desc = "Description"
    stat = "Status"
    created = "Created At"
    updated = "Updated At"

    print("="*92)
    print(f"| {index.center(3):3} | {desc.center(30):30} | {stat.center(11):11} | {created.center(16):16} | {updated.center(16):16} |")
    print("-"*92)

    for data in current_data:
        if status == "all":
            index = data["id"]
            desc = desc_limit(data["description"])
            stat = data["status"]
            created = data["created_at"]
            updated = data["updated_at"]
        else:
            if data["status"] == status:
                index = data["id"]
                desc = desc_limit(data["description"])
                stat = data["status"]
                created = data["created_at"]
                updated = data["updated_at"]
            else:
                continue

        print(f"| {str(index).center(3):3} | {desc:.30} | {stat:11} | {created:16} | {updated:16} |")
    print("="*92)


initiate_db()

option = sys.argv[1].split("-")

match option[0]:
    case "add": add(sys.argv[2])
    case "update": update(int(sys.argv[2]), sys.argv[3])
    case "mark": mark(int(sys.argv[2]), sys.argv[1].split("-"))
    case "delete": delete(int(sys.argv[2]))
    case "list": task_list(get_status())
    case _: print("invalid command.")
    