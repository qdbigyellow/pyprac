# https://mp.weixin.qq.com/s/8fpHUc0W9UqA4ic7flZLDw

#  In general
#  a better data stracture > func([list comprehension]) > func(generator) >  for x in list > for range() > while

########
# Sum the list
########
def sum_sqr_5(arr):
    return sum([x ** 2 for x in arr])

def sum_sqr_4(arr):
    return sum(x ** 2 for x in arr)

def sum_sqr_3(arr):
    return sum(map(lambda x: x**2, arr))

def sum_sqr_2(arr):
    res = 0
    for x in arr:
        res += x ** 2
    return res

def sum_sqr_1(arr):
    res = 0
    for i in range(len(arr)):
        res += arr[i] ** 2
    return res

def sum_sqr_0(arr):
    res = 0
    n = len(arr)
    i = 0
    while i < n:
        res += arr[i] ** 2
        i += 1
    return res


#######
# concat string
###
def concat_strings_4(strings):
    return "".join([x[:3] for x in strings])

def concat_strings_3(strings):
    return "".join(x[:3] for x in strings)

def concat_strings_2(strings):
    res = ""
    for x in strings:
        res += x[:3]
    return res

def concat_strings_1(strings):
    res = ""
    for i in range(len(strings)):
        res += strings[i][:3]
    return res

def concat_strings_0(strings):
    res = ""
    n = len(strings)
    i = 0
    while i < n:
        res += strings[i][:3]
        i += 1
    return res


###########
# filter odd number
##############

def filter_odd_5(arr):
    return [x for x in arr if x % 2]

def filter_odd_4(arr):
    return list((x for x in arr if x % 2))

def filter_odd_3(arr):
    # filter() is very slow.
    return list(filter(lambda x: x % 2, arr))

def filter_odd_2(arr):
    res = []
    for x in arr:
        if x % 2:
            res.append(x)
    return res

def filter_odd_1(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] % 2:
            res.append(arr[i])
        i += 1
    return res

def filter_odd_0(arr):
    res = []
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] % 2:
            res.append(arr[i])
        i += 1
    return res


################
# add to list
################
def arr_sum_4(arr1, arr2):
    return [x + y for x, y in zip(arr1, arr2)]

def arr_sum_3(arr1, arr2):
    # 避免arr[i]的变量类型检查带来的额外开销
    res = []
    for x, y in zip(arr1, arr2):
        res.append(x + y)
    return res

def arr_sum_2(arr1, arr2):
    res = arr1.copy()
    for i, x in enumerate(arr2):
        res[i] += x
    return res

def arr_sum_1(arr1, arr2):
    res = []
    for i in range(len(arr1)):
        res.append(arr1[i] + arr2[i])
    return res

def arr_sum_0(arr1, arr2):
    i = 0
    n = len(arr1)
    res = []
    while i < n:
        res.append(arr1[i] + arr2[i])
        i += 1
    return res


###################
# check identical element among two lists
####################
def n_common_5(arr1, arr2):
    return len(set(arr1) & set(arr2))

def n_common_4(arr1, arr2):
    # 将数组用.sort方法排序，再进行单层循环遍历。把时间复杂度从O(n2)降低到O(nlogn)
    arr1.sort()
    arr2.sort()
    res = i = j = 0
    m, n = len(arr1), len(arr2)
    while i < m and j < n:
        if arr1[i] == arr2[j]:
            res += 1
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1
    return res

def n_common_3(arr1, arr2):
    res = 0
    for x in arr1:
        if x in arr2:
            res += 1
    return res


def n_common_2(arr1, arr2):
    # 避免arr[i]的变量类型检查带来的额外开销
    res = 0
    for x in arr1:
        for y in arr2:
            if x == y:
                res += 1
    return res

def n_common_1(arr1, arr2):
    # 避免i += 1的变量类型检查带来的额外开销
    res = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                res += 1
    return res

def n_common_0(arr1, arr2):
    res = 0
    i = 0
    m = len(arr1)
    n = len(arr2)
    while i < m:
        j = 0
        while j < n:
            if arr1[i] == arr2[j]:
                res += 1
            j += 1
        i += 1
    return res
