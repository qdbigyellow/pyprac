from itertools import product
from time import perf_counter

# use product to get all combination of two list

def _cross_sum(arr1, arr2):
    for x in arr1:
        for y in arr2:
            yield x + y

def cross_sum(arr1, arr2):
    return list(_cross_sum(arr1, arr2))


def fast_cross_sum(arr1, arr2):
    return [x + y for x, y in product(arr1, arr2)]


if __name__ == "__main__":
    arr1 = list(range(100))
    arr2 = list(range(100))    
    start = perf_counter()
    cross_sum(arr1, arr2)
    duration_slow = perf_counter() - start
    print('own product', duration_slow)

    start = perf_counter()
    fast_cross_sum(arr1, arr2)
    duration_fast = perf_counter() - start
    print('itertool product', duration_fast)
    
    improvement = duration_slow / duration_fast
    print(improvement)
