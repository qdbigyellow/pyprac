from itertools import permutations
from time import perf_counter

from random import randint


# use permutation to generate all possible combination to get k elements from array

def _get_permutations(arr, k, i):
    if i == k:
        return [arr[:k]]
    res = []
    for j in range(i, len(arr)):
        arr_cpy = arr.copy()
        arr_cpy[i], arr_cpy[j] = arr_cpy[j], arr_cpy[i]
        res += _get_permutations(arr_cpy, k, i + 1)
    return res

def get_permutations(arr, k):
    return _get_permutations(arr, k, 0)

def fast_get_permutations(arr, k):
    return list(permutations(arr, k))


if __name__ == "__main__":
    arr = list(range(10))
    k = 5
    
    start = perf_counter()
    get_permutations(arr, k)
    duration_slow = perf_counter() - start
    print('own permutation', duration_slow)

    start = perf_counter()
    fast_get_permutations(arr, k)
    duration_fast = perf_counter() - start
    print('itertool permutation', duration_fast)
    
    improvement = duration_slow / duration_fast
    print(improvement)
