#!/usr/bin/python3
'''A python script that returns info about an employee's TODO list
progress
'''
import json
import requests


def get_todo_progress(employee_id):
    '''fetches employee todo progress

    Args:
        employee_id (int): Employee ID
    '''
    # fetch employee info
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_info = requests.get(f'{api_url}/users/{employee_id}')
    # raise stored HTTPError, if one occured
    employee_info.raise_for_status()
    employee_data = employee_info.json()
    employee_name = employee_data.get("username")
    # rectified error: "" instead of ''

    # fetch todos for employee
    todos = requests.get(f'{api_url}/users/{employee_id}/todos')
    todos.raise_for_status()
    todos_data = todos.json()

    # handle exportation to JSON here
    tasks = []
    for todo in todos_data:
        tasks.append({
            'task': todo.get("title"),
            'completed': todo.get("completed"),
            'username': employee_name
        })

    data = {employee_id: tasks}
    filename = f'{employee_id}.json'
    with open(filename, 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <employee_id>')
        sys.exit(1)

    try:
        employee_id = sys.argv[1]
    except ValueError:
        print('Employee ID must be an integer.')
        sys.exit(1)

    # run function
    get_todo_progress(employee_id)
