# shows how the decorator works
# 1. Run c_c_func = b_decorator(c_func), c_c_func is b_wrapper
# 2. run c_func = a_decorator(c_c_func), c_func is a_wrapper
# 3. run c_func(100, 200) which is a_wrapper
# 4. 0


def a_decorator(func):
    print("A decorator, outer, 1")
    def wrapper(a, b):
        print("A decorator, inner, 1")
        result = func(a, b)
        print("A decorator, inner, 2")
        return result
    print("A decorator, outer, 2")
    return wrapper


def b_decorator(func):
    print("B decorator, outer, 1")
    def wrapper(a, b):
        print("B decorator, inner, 1")
        result = func(a, b)
        print("B decorator, inner, 2")
        return result
    print("B decorator, outer, 2")
    return wrapper
    
        
@a_decorator
@b_decorator
def c_func(a, b):
    return a + b

res = c_func(100, 200)
print(res)