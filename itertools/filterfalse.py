from itertools import filterfalse
from time import perf_counter




# use filterfalse to remove all the elements where the condition is false
# itertools filterfalse is

def get_even_nums(arr):
    return [x for x in arr if x % 2 == 0]

def fast_get_even_nums(arr):
    return list(filterfalse(lambda x: x % 2, arr))


if __name__ == "__main__":
    arr = list(range(10000))
    
    start = perf_counter()
    get_even_nums(arr)
    duration_slow = perf_counter() - start
    print('own filterfalse', duration_slow)

    start = perf_counter()
    fast_get_even_nums(arr)
    duration_fast = perf_counter() - start
    print('itertool filterfalse', duration_fast)
    
    improvement = duration_slow / duration_fast
    print(improvement)
