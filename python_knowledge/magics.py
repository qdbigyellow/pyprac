# https://mp.weixin.qq.com/s/7NUbyZxCwC62yw_0jpe6ZA

# 构造与初始化
# __init__,  __new__,  __del__
# 类的表示
# __str__, __repr__,  __unicode__, __hash__, __eq__,  __bool__
# 访问控制
# __setattr__,  __get_attr__, __delattr__,  __getattribute__
# 比较操作
# 容器类操作
# 可调用对象
# 序列化



class Person(object):
    
    # __new__ 会在对象实例化时第一个被调用，然后才会调用 __init__，它们的区别如下：
    # __new__ 的第一个参数是 cls，而 __init__ 的第一个参数是 self
    # __new__ 返回值是一个实例对象，而 __init__ 没有任何返回值，只做初始化操作
    # __new__ 由于返回的是一个实例对象，所以它可以给所有实例进行统一的初始化操作

    def __new__(cls, *args, **kwargs):
        print "call __new__"
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print "call __init__"
        self.name = name
        self.age = age

p = Person("张三", 20)


class Singleton(object):
    """由于 __new__ 优先于 __init__ 调用，而且它返回的是一个实例，所以我们可以利用这个特性，
    在 __new__ 方法中，每次返回同一个实例来实现一个单例类"""
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MySingleton(Singleton):
    pass

a = MySingleton()
b = MySingleton()

assert a is b # True


class g(float):
    """千克转克
    当我们需要继承内置类时，例如想要继承 int、str、tuple，就无法使用 __init__ 来初始化了，只能通过 __new__ 来初始化数据
    """
    def __new__(cls, kg):
        return float.__new__(cls, kg * 2)

a = g(50) # 50千克转为克
print a   # 100
print a + 100 # 200 由于继承了float，所以可以直接运算，非常方便！

class Person(object):
    # Python 是通过引用计数来进行垃圾回收的，如果这个实例在执行 del 时，还被其他对象引用，那么就不会触发执行 __del__ 方法
    def __del__(self):
        print '__del__'
        
a = Person()
print 'exit'

# Output:
# exit
# __del__

a = Person()
del a    # 手动销毁对象, 由于实例没有被其他对象所引用，当我们手动销毁这个实例时，__del__ 被调用后程序正常退出
print 'exit'

# Output:
# __del__
# exit

a = Person()
b = a   # b引用a
del a   # 手动销毁 不触发__del__
print 'exit'

# Output:
# exit
# __del__



# __str__ 强调可读性，而 __repr__ 强调准确性 / 标准性
# __str__ 的目标人群是用户，而 __repr__ 的目标人群是机器，__repr__ 返回的结果是可执行的，通过 eval(repr(obj)) 可以正确运行
# 占位符 %s 调用的是 __str__，而 %r 调用的是 __repr__ 方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 格式化 友好对用户展示
        return 'name: %s, age: %s' % (self.name, self.age)

    def __repr__(self):
        # 标准化展示
        return "Person('%s', %s)" % (self.name, self.age)

person = Person('zhangsan', 20)

# 强调对用户友好
print str(person)       # name: zhangsan, age: 20 
print '%s' % person     # name: zhangsan, age: 20

# 强调对机器友好 结果 eval 可执行
print repr(person)      # Person('zhangsan', 20)
print '%r' % person     # Person('zhangsan', 20)

# __repr__ 在表示类时，是一级的，如果只定义它，那么 __str__ = __repr__。
# 而 __str__ 展示类时是次级的，如果没有定义 __repr__，那么 repr(person) 将会展示缺省的定义。


#__hash__ 方法返回一个整数，用来表示实例对象的唯一标识，配合 __eq__ 方法，可以判断两个对象是否相等：
class Person(object):
    def __init__(self, uid):
        self.uid = uid
        
    def __repr__(self):
        return 'Person(%s)' % self.uid
        
    def __hash__(self):
        return self.uid
    
    def __eq__(self, other):
        return self.uid == other.uid
    
p1 = Person(1)
p2 = Person(1)
p1 == p2    # True

p3 = Person(2)
print set([p1, p2, p3]) # 根据唯一标识去重输出 set([Person(1), Person(2)])


class Person(object):
    def __init__(self, uid):
        self.uid = uid

    def __bool__(self):
        return self.uid > 10
    
p1 = Person(1)
p2 = Person(15)
print bool(p1)  # False
print bool(p2)  # True




class Person(object):

    def __setattr__(self, key, value):
        """属性赋值
        当我们在给一个对象进行属性赋值时，都会经过这个方法
        通过 __setattr__ 方法，我们可以非常方便地对属性赋值进行控制。
        """
        if key not in ('name', 'age'):
            return
        if key == 'age' and value < 0:
            raise ValueError()
        super(Person, self).__setattr__(key, value)

    def __getattr__(self, key):
        """访问某个不存在的属性
        __getattr__ 只有在访问「不存在的属性」时才会被调用，
        """
        return 'unknown'

    def __delattr__(self, key):
        """删除某个属性
        当删除对象的某个属性时，这个方法会被调用，所以它一般会用在删除属性前的校验场景中使用。
        """
        if key == 'name':
            raise AttributeError()
        super(Person, self).__delattr__(key)

    def __getattribute__(self, key):
        """所有属性/方法调用都经过这里
        __getattr__ 只有在访问不存在的属性时被调用，而 __getattribute__ 在访问任意属性时都会被调用
        __getattr__ 只针对属性访问，而__getattribute__ 不仅针对所有属性访问，还包括方法调用
        """
        if key == 'money':
            return 100
        if key == 'hello':
            return self.say
        return super(Person, self).__getattribute__(key)

    def say(self):
        return 'hello'
    
p1 = Person()
p1.name = 'zhangsan' # 调用__setattr__
p1.age = 20          # 调用__setattr__
print p1.name        # zhangsan
print p1.age         # 20

setattr(p1, 'name', 'lisi') # 调用__setattr__
setattr(p1, 'age', 30)      # 调用__setattr__
print p1.name               # lisi
print p1.age                # 30

p1.gender = 'male'  # __setattr__中忽略对gender赋值
print p1.gender     # gender不存在 所以会调用__getattr__返回unknown

print p1.money      # money不存在 在__getattribute__中返回100

print p1.say()      # hello
print p1.hello()    # hello 调用__getattribute__ 间接调用say方法

del p1.name         # __delattr__中引发AttributeError

p2 = Person()
p2.age = -1         # __setattr__中引发ValueError


# __cmp__
# __eq__
# __ne__
# __lt__
# __gt__

class Person(object):
    def __init__(self, uid):
            self.uid = uid

    def __cmp__(self, other):
        if self.uid == other.uid:
            return 0
        if self.uid > other.uid:
            return 1
        return -1

p1 = Person(1)
p2 = Person(2)
print p1 > p2 # False
print p1 < p2 # True
print p1 == p2 # False


class Person(object):

    def __init__(self, uid, name, salary):
        self.uid = uid
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        """对象 == 判断"""
        return self.uid == other.uid

    def __ne__(self, other):
        """对象 != 判断"""
        return self.uid != other.uid

    def __lt__(self, other):
        """对象 < 判断 根据len(name)"""
        return len(self.name) < len(other.name)

    def __gt__(self, other):
        """对象 > 判断 根据alary"""
        return self.salary > other.salary


p1 = Person(1, 'zhangsan', 1000)
p2 = Person(1, 'lisi', 2000)
p3 = Person(1, 'wangwu', 3000)

print p1 == p1 # uid 是否相同
print p1 != p2 # uid 是否不同
print p2 < p3 # name 长度比较
print p3 > p2 # salary 比较


#容器类操作: 字典 元组 列表 字符串 这些都是容器类型。因为它们都是「可迭代」的。可迭代是因为，它们都实现了容器协议
# __setitem__
# __getitem__
# __delitem__
# __len__
# __iter__
# __contains__
# __reversed__

class MyList(object):
    """自己实现一个list"""

    def __init__(self, values=None):
        # 初始化自定义list
        self.values = values or []

    def __setitem__(self, key, value):
        # 添加元素
        self.values[key] = value

    def __getitem__(self, key):
        # 获取元素
        return self.values[key]

    def __delitem__(self, key):
        # 删除元素
        del self.values[key]

    def __len__(self):
        # 自定义list的元素个数
        return len(self.values)

    def __iter__(self):
        # 可迭代
        return self

    def __next__(self):
        # 迭代的具体细节
        # 如果__iter__返回self 则必须实现此方法
        if self._index >= len(self.values):
            raise StopIteration()
        value = self.values[self._index]
        self._index += 1
        return value

    def __contains__(self, key):
        # 元素是否在自定义list中
        return key in self.values

    def __reversed__(self):
        # 反转
        return list(reversed(self.values))

# 初始化自定义list
my_list = MyList([1, 2, 3, 4, 5])

print my_list[0]      # __getitem__
my_list[1] = 20       # __setitem__

print 1 in my_list      # __contains__
print len(my_list)      # __len__

print [i for i in my_list]  # __iter__
del my_list[0]              # __del__

reversed_list = reversed(my_list) # __reversed__
print [i for i in reversed_list]  # __iter__



# 可调用对象
class Circle(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y

c = Circle(10, 20)  # __init__
print c.x, c.y     # 10 20

c(100, 200)         # 调用instance() 触发__call__
print c.x, c.y      # 100 200


# 序列化
class Person(object):

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __getstate__(self):
        # 执行 pick.dumps 时 忽略 age 属性
        return {
            'name': self.name,
            'birthday': self.birthday
        }

    def __setstate__(self, state):
        # 执行 pick.loads 时 忽略 age 属性
        self.name = state['name']
        self.birthday = state['birthday']

person = Person('zhangsan', 20, date(2017, 2, 23))
pickled_person = pickle.dumps(person) # __getstate__

p = pickle.loads(pickled_person) # __setstate__
print p.name, p.birthday

print p.age # AttributeError: 'Person' object has no attribute 'age'