"""Using built-in functions"""

from operator import itemgetter

def sort_tasks(tasks):
    """Sort tasks by priority"""
    return sorted(tasks, key=lambda task: task[1])


def sort_tasks_ig(tasks):
    """Sort tasks by priority"""
    # itemgetter is a build-in written in C, which is faster than own code. 
    return sorted(tasks, key=itemgetter(1))    


if __name__ == '__main__':
    import random

    random.seed(353)
    tasks = [(f'task{i}', i) for i in range(1000)]
    random.shuffle(tasks)
