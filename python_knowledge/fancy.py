import funcy as fc

# https://mp.weixin.qq.com/s/a_phmcfPb5HEBodc4wpkJg

def fc_cnt():
    for i in fc.count():
        print(i + '\r')
        if i > 10:
            break
 
def fc_flttn():
    l1 = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
    print(list(fc.flatten(l1)))

def fc_interpose():
    print(list(fc.interpose("haha", [1, 2, 3])))
    

def fc_remove():
    print(list(fc.remove(lambda x: x == None or x == '',  [None, '', 1, 2, 3, '', 4, None])))
    

def fc_without():
    print(list(fc.without(list(range(10))*2, 2, 5, 7, 9)))
    
def fc_groupby():
    """[return stat is a defultdict]
    """
    stat = fc.group_by(len, ['a', 'bb', 'ccc', 'd', 'ee', 'fff', 'gggg', 'hhhh'])    
    for s in stat.values():
        print(s)

def fc_partition():
    "the reside will be discarded"
    print(list(fc.partition(4, list(range(17)))))

def fc_chunks():
    "the reside will be kept"
    print(list(fc.chunks(4, list(range(17)))))
        
def fc_pairwise():
    "the reside will be kept"
    print(list(fc.pairwise(range(17))))

def fc_merge():
    print("list", fc.merge([1, 2, 3], [1, 2, 3], [1, 2, 3]))
    print("dict", fc.merge({1:1, 2:2}, {3:3, 4:4}, {5:5, 6:6}))
    print("tuple", fc.merge((1,2), (2, 3, 4), (5, 6)))
    print("set", fc.merge({1, 2}, {2, 3, 4}, {4, 5, 6}))
    print("list_of_dict", fc.merge(*[{1:1, 2:2}, {3:3, 4:4}, {5:5, 6:6}]))
    
def fc_silent():
    print(fc.silent(int)('1'))
    print(fc.silent(int)('abc') == None)

def fc_ignore():
    fc.ignore(errors=(ValueError, ZeroDivisionError), default="error")(lambda x: int(x)/(int(x)-1))('1')

import math
def jobslow(x):
    return round(math.log(x ** 2 / 10) / 4)

@fc.memoize
def jobfast(x):
    return round(math.log(x ** 2 / 10) / 4)

def call_fcfast():
    """momoize decorator will remember the input and output, so it could be reuse next time it is called.
    """
    _ = [jobfast(10) for i in range(10000000)]    
    print(jobfast.memory)
    jobfast.memory.update({(2,): jobfast(2)})
    jobfast.memory.clear()

def fc_tap():
    """help to print in list comprehension. 
    """
    [(fc.tap(i, 'x'), fc.tap(i**2, 'x^2')) for i in range(3)]
    
@fc.once
def fc_once(x):
    x = x + 1
    return x

def call_fc_once():
    print(fc_once(5))
    print(fc_once(5))

if __name__ == "__main__":
    call_fcfast()