# https://mp.weixin.qq.com/s/niwGXv4RuLWpD4QkEzuVew

# generator

def gen(n):
    for i in range(n):
        yield i
        

g = gen(5)      # 创建一个生成器, gen 中的代码其实并没有执行，此时我们只是创建了一个「生成器对象」，它的类型是 generator。
print(g)        # <generator object gen at 0x10bb46f50>
print(type(g))  # <type 'generator'>

# 创建生成器时，这个 5 个元素其实还并没有产生，什么时候产生呢？只有在执行 for 循环遇到 yield 时，才会依次生成每个元素。



def gen2():
    i = 1
    while True:
        j = yield i
        i *= 2
        if j == -1:
            break


# 这段代码一直循环的原因在于，它无法执行到 j == -1 这个分支里 break
for i in gen2():
    print(i)
    time.sleep(1)
    if i > 100:
        gent2.send(-1)
# Solution:  send(), 从外部向generator里面送一个值

# Throw: 外部向生成器内部传入一个异常
# 比如生成器内部有异常处理的命令，可以通过传入异常来执行
def gen3():
    try:
        yield 1
    except ValueError:
        yield 'ValueError'
    finally:
        print('finally')

g = gen3()   # 创建一个生成器
print(g.__next__()) # 1
# 向生成器内部传入异常 返回ValueError
print(g.throw(ValueError))



# Example

# 错误写法， 拼凑起一个大的list， 
def gen_list():
    # 多个逻辑块 组成生成一个列表
    result = []
    for i in range(10):
        result.append(i)
    for j in range(5):
        result.append(j * j)
    for k in [100, 200, 300]:
        result.append(k)
    return result
    
for item in gen_list():
    print(item)


# 正确写法，用生成器，避免了用append想 list 里面追加元素
def gen_list():
    # 多个逻辑块 使用yield 生成一个列表
    for i in range(10):
        yield i
    for j in range(5):
        yield j * j
    for k in [100, 200, 300]:
        yield k
        
for item in gen_list():
    print(i)
    
    
# coroutine

# consumer是一个生成器
def consumer():
    i = None
    while True:
        # 拿到 producer 发来的数据
        j = yield i  # 2c.  等待 i
        print('consume %s' % j)  # 4  consumer 函数被唤醒，从 j = yield i 处继续开始执行，并且接收到 producer 传来的数据赋值给 j，然后打印输出，直到再次执行到 yield 处，

def producer(c: generator):
    c.__next__()  # 2b： c.__next()__ 会启动生成器 consumer 直到代码运行到 j = yield i 处，此时 consumer 第一次执行完毕，返回
    for i in range(5):  # 5.  执行循环
        print('produce %s' % i) 
        # 发数据给 consumer
        c.send(i)   # 3：  利用生成器的 send 方法，向 consumer 发送数据
    c.close()  #6 退出

c = consumer()  # 1. c = consumer() 创建一个生成器对象
producer(c)     # 2a 