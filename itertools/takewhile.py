from itertools import takewhile
from time import perf_counter




# use takewhile to get the elements until the elements meets a condition

def cond_sum(arr, target):
    res = 0
    for x in arr:
        if x > target:
            break
        res += x
    return res

def fast_cond_sum(arr, target):
    return sum(takewhile(lambda x: x <= target, arr))



if __name__ == "__main__":
    arr = list(range(10000))
    target = 5000
    start = perf_counter()
    cond_sum(arr, target)
    duration_slow = perf_counter() - start
    print('own takewhile', duration_slow)

    start = perf_counter()
    fast_cond_sum(arr, target)
    duration_fast = perf_counter() - start
    print('itertool while', duration_fast)
    
    improvement = duration_slow / duration_fast
    print(improvement)
