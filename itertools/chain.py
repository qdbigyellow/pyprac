from itertools import chain
from time import perf_counter

# use chain to concat multi-dimension array to one dimension array

def _flatten(arr2d):
    for arr in arr2d:
        for x in arr:
            yield x

def flatten(arr2d):
    return list(_flatten(arr2d))


def fast_flatten(arr2d):
    return list(chain(*arr2d))


if __name__ == "__main__":
    arr2d = [[x + y * 100 for x in range(100)] for y in range(100)]
    
    start = perf_counter()
    f = flatten(arr2d)
    duration_slow = perf_counter() - start
    print('own chain', duration_slow)
    print(f)

    start = perf_counter()
    ff = fast_flatten(arr2d)
    duration_fast = perf_counter() - start
    print('itertool chain', duration_fast)
    print(ff) 
    
    improvement = duration_slow / duration_fast
    print(improvement)
