#!/usr/bin/python3
'''A python script that returns info about an employee's TODO list
progress
'''
import json
import requests


def get_todo_progress_all():
    '''fetches all employee todo progress'''
    # fetch all employees
    api_url = 'https://jsonplaceholder.typicode.com'
    employees_info = requests.get(f'{api_url}/users')
    # raise stored HTTPError, if one occured
    employees_info.raise_for_status()
    employees_data = employees_info.json()

    # initialise empty dictionary to store tasks
    all_tasks = {}

    # fetch todos for each employee
    for employee in employees_data:
        # get employee id and name info
        employee_id = employee.get("id")
        employee_name = employee.get("username")

        # fetch todos for current employee
        todos = requests.get(f'{api_url}/users/{employee_id}/todos')
        todos.raise_for_status()
        todos_data = todos.json()

        # handle tasks for employee here
        tasks = []
        for todo in todos_data:
            tasks.append({
                'username': employee_name,
                'task': todo.get("title"),
                'completed': todo.get("completed"),
            })

        all_tasks[employee_id] = tasks

    # handle all tasks export to JSON
    filename = 'todo_all_employees.json'
    with open(filename, 'w', encoding='UTF-8') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    # run function
    get_todo_progress_all()
