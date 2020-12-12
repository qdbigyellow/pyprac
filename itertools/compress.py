from itertools import compress
from time import perf_counter

from random import randint


# use compress instead homemade zip-based selector to compress data

def select_data(data, selectors):
    return [x for x, y in zip(data, selectors) if y]

def fast_select_data(data, selectors):
    return list(compress(data, selectors))


if __name__ == "__main__":
    data = list(range(10000))
    selectors = [randint(0, 1) for _ in range(10000)]

    start = perf_counter()
    select_data(data, selectors)
    duration_slow = perf_counter() - start
    print('own compress', duration_slow)

    start = perf_counter()
    fast_select_data(data, selectors)
    duration_fast = perf_counter() - start
    print('itertool compress', duration_fast)
    
    improvement = (duration_slow - duration_fast) / duration_slow * 100
    print(improvement)
