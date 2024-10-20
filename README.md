# Tasker: CLI Task Tracker App
Tasker is a task tracker application based on command-line interface. This application allows users to add, delete, update, and list tasks using various commands. It provides a straightforward way to interact with a task database using a simple CLI interface, making it an ideal tool for both personal and professional task tracking.

## Features
Tasker have various function to help users track and manage their task:
- **Add a task**: Users can add task by providing description. each newly added task will be given unique ID and set to "todo" status.
- **update a task**: Users can change their task description by providing the task ID and the new description.
- **Mark a task**: Users can set their task status either as "done" or "in-progress" by providing the task ID.
- **Delete a task**: Users can remove task from the list by providing task ID.
- **List a task**: Users can list all their tasks and filter them based on the status by providing the status.

## Installation & Usage
1. Installation
    To install the application clone the git repository using `git clone https://github.com/subh1l/tasker.git`

2. Usage
    1. Open your terminal.

    2. Go to the directory where the main file is.

    3. run the project.

        - Adding task: `./tasker.py add "task description"`
            Example: `/tasker.py add "wash the dishes."`   
            Output: New task with correspoding ID added to the list.

        - Updating task: `./tasker.py update task_ID "new task description"`
            Example: `./tasker.py update 1 "wash the dishes and cook dinner."`
            Output: Description of task with correspoding ID will change to the new description.

        - Marking task: `./tasker.py mark* (task ID)`
            *Valid argument: "-done" or "-in-progress"
            Example: `./tasker.py mark-done 1"`
            Output: Status of task with corresponding ID will change to the new status.

        - Deleting task: `./tasker.py delete (task ID)`
            Example: `./tasker.py delete 1`
            Output: Task with corresponding ID is deleted.
        
        - Listing task: `./tasker.py list *"`
            *Valid command: "todo", "in-progress", "done", or leave it empty to show all task
            Example: 
            - `./tasker.py list`
            - `./tasker.py list todo`
            Output:
            - List all task in database
            - List all task with status todo in database.
            
        
## Project Link
to see more information click this [link](https://roadmap.sh/projects/task-tracker)
