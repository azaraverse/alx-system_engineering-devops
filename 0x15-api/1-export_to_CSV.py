#!/usr/bin/python3
'''A python script that returns info about an employees' TODO list
progress
'''
import csv
import requests


def get_todo_progress(employee_id):
    '''fetches employee todo progress

    Args:
        employee_id (int): Employee ID
    '''
    # fetch employee info
    api_url = f'https://jsonplaceholder.typicode.com'
    employee_info = requests.get(f'{api_url}/users/{employee_id}')
    # raise stored HTTPError, if one occured
    employee_info.raise_for_status()
    employee_data = employee_info.json()
    employee_name = employee_data.get("name")
    # rectified error: "" instead of ''

    # fetch todos for employee
    todos = requests.get(f'{api_url}/users/{employee_id}/todos')
    todos.raise_for_status()
    todos_data = todos.json()

    # count completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = 0
    for todo in todos_data:
        if todo.get("completed"):  # rectified error: "" instead of ''
            completed_tasks += 1

    # display progress
    print(
        f'Employee {employee_name} is done with tasks'
        f'({completed_tasks}/{total_tasks}):'
    )
    for todo in todos_data:
        if todo.get("completed"):  # rectified error: "" instead of ''
            print(f"\t {todo.get('title')}")

    # handle exportation to CSV here
    filename = f'{employee_id}.csv'
    with open(filename, 'w', encoding='UTF-8') as csv_file:
        csv_write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_write.writerow(
            ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            )
        for todo in todos_data:
            csv_write.writerow(
                [
                    employee_id,
                    employee_name,
                    todo.get("completed"),
                    todo.get("title")
                ]
            )


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
