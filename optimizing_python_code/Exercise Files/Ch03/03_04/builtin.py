"""Using built-in functions"""
# PYthon sorts tuple in lexicographical order (by name)
# Python string compare '3' > '200'  is true

from operator import itemgetter

def sort_tasks(tasks):
    """Sort tasks by priority"""
    # Key is a functin that get the object we'd like to compare, and 
    # return the value represent of that object
    #
    # sorted(Sequence, key=func)  e.g  sorted(some_list, key=len) will sort the list by the element's length
    #
    return sorted(tasks, key=lambda task: task[1])   


if __name__ == '__main__':
    import random

    random.seed(353)
    tasks = [(f'task{i}', i) for i in range(1000)]   # A tuple
    random.shuffle(tasks)
