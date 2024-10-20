#!/usr/bin/env python3

import sys

import func

func.initiate_db()

option = sys.argv[1].split("-")

match option[0]:
    case "add": func.add(sys.argv[2])
    case "update": func.update(int(sys.argv[2]), sys.argv[3])
    case "mark": func.mark(int(sys.argv[2]), sys.argv[1].split("-"))
    case "delete": func.delete(int(sys.argv[2]))
    case "list": func.task_list(func.get_status())
    case _: print("invalid command.")
    