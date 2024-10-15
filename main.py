#!/usr/bin/env python3

import os
import sys
import datetime
import json

data_path = os.path.dirname(__file__) + "/data.json"

def __init__():
    if not os.path.exists(data_path):
        with open(data_path, "w") as file:
            json.dump([], file)

def get_id():
    with open(data_path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
        list_of_ids = []
        for task in data:
            list_of_ids.append(task["id"])
    for i in range(0, 100):
        if i not in list_of_ids:
            return i
            break

def add():
    with open(data_path, "r") as file:        
        try:
            current_data = json.load(file)
        except json.JSONDecodeError:
            current_data = []
    data = {}
    data["id"] = get_id()
    data["description"] = sys.argv[2]
    data["status"] = "todo"
    data["created_at"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    data["updated_at"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    current_data.append(data)
    with open(data_path, "w") as file:
        json.dump(current_data, file, indent=4)

def update():
    with open(data_path, "r") as file:
        try:
            current_data = json.load(file)
        except json.JSONDecodeError:
            current_data = []
    for task in current_data:
        if task["id"] == int(sys.argv[2]):
            task["description"] = sys.argv[3]
            task["updated_at"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            break
    with open(data_path, "w") as file:
        json.dump(current_data, file, indent=4)

def delete():
    with open(data_path, "r") as file:
        try:
            current_data = json.load(file)
        except json.JSONDecodeError:
            pass
    for task in current_data:
        if task["id"] == int(sys.argv[2]):
            current_data.remove(task)
            with open(data_path, "w") as file:
                json.dump(current_data, file, indent=4)

def mark():
    with open(data_path, "r") as file:
        try:
            current_data = json.load(file)
        except json.JSONDecodeError:
            pass
    for task in current_data:
        if task["id"] == int(sys.argv[2]):
            task["status"] = sys.argv[3]
    with open(data_path, "w") as file:
            json.dump(current_data, file, indent=4)
        
def list_all():
    with open(data_path, "r")as file:
        current_data = json.load(file)
    index = "Id"
    desc = "Description"
    stat = "Status"
    ca = "Created At"
    ua = "Updated At"
    print("="*91)
    print(f"| {index.center(2):2} | {desc.center(30):30} | {stat.center(11):11} | {ca.center(16):16} | {ua.center(16):16} |")
    print("-"*91)
    for data in current_data:
        index = data["id"]
        desc = data["description"]
        stat = data["status"]
        ca = data["created_at"]
        cu = data["updated_at"]
        print(f"| {index:2} | {desc:30} | {stat:11} | {ca:16} | {ca:16} |")
    print("="*91)

def list_done():
    with open(data_path, "r")as file:
        current_data = json.load(file)
    index = "Id"
    desc = "Description"
    stat = "Status"
    ca = "Created At"
    ua = "Updated At"
    print("="*94)
    print(f"| {index.center(2):2} | {desc:30} | {stat:11} | {ca:14} | {ua:14} |")
    print("-"*94)
    for data in current_data:
        if data["status"] == "done":
            index = data["id"]
            desc = data["description"]
            stat = data["status"]
            ca = data["created_at"]
            cu = data["updated_at"]
            print(f"| {index:2} | {desc:30} | {stat:11} | {ca:14} | {cu:14} |")

def list_not_done():
    with open(data_path, "r")as file:
        current_data = json.load(file)
    index = "Id"
    desc = "Description"
    stat = "Status"
    ca = "Created At"
    ua = "Updated At"
    print("="*94)
    print(f"| {index.center(2):2} | {desc:30} | {stat:11} | {ca:14} | {ua:14} |")
    print("-"*94)
    for data in current_data:
        if data["status"] == "todo":
            index = data["id"]
            desc = data["description"]
            stat = data["status"]
            ca = data["created_at"]
            cu = data["updated_at"]
            print(f"| {index:2} | {desc:30} | {stat:11} | {ca:14} | {cu:14} |")

def list_in_progress():
    with open(data_path, "r")as file:
        current_data = json.load(file)
    index = "Id"
    desc = "Description"
    stat = "Status"
    ca = "Created At"
    ua = "Updated At"
    print("="*91)
    print(f"| {index.center(2):2} | {desc:30} | {stat:11} | {ca:16} | {ua:16} |")
    print("-"*91)
    for data in current_data:
        if data["status"] == "in-progress":
            index = data["id"]
            desc = data["description"]
            stat = data["status"]
            ca = data["created_at"]
            cu = data["updated_at"]
            print(f"| {index:2} | {desc:30} | {stat:11} | {ca:16} | {cu:16} |")
    print("="*91)

list_all()