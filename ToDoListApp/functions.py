FILEPATH = "tasks.txt"


def get_tasks(filepath=FILEPATH):
    """ Read a task and return a list tasks
    from the tasks text file.
    """
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local

def write_tasks(tasks_arg, filepath=FILEPATH):
    """ Write a task and return a list of tasks
    from the tasks text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)