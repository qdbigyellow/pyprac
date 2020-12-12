from itertools import accumulate 
from time import perf_counter

# Use itertools.accumulate to sum up list. 

def _accumulate_list(arr):
    tot = 0
    for x in arr:
        tot += x
        yield tot

def accumulate_list(arr):
    return list(_accumulate_list(arr))

def fast_accumulate_list(arr):
    return list(accumulate(arr))


if __name__ == "__main__":
    arr = list(range(1000))
    start = perf_counter()
    accumulate_list(arr)
    duration_slow = perf_counter() - start
    print('own accumulate', duration_slow)

    start = perf_counter()
    fast_accumulate_list(arr)
    duration_fast = perf_counter() - start
    print('itertool accumulate', duration_fast)
    
    improvement = (duration_slow  - duration_fast) / duration_slow * 100
    print(improvement)
    