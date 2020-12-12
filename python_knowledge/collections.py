import collections

##################33
# Counter
# 统计字符出现的次数
print(collections.Counter('hello world'))
# 统计单词个数
r = collections.Counter('hello world hello lucy'.split())
print(r)
print(r["hello"])
print([x for x in r.elements()])
print(r.most_common())
r1 = collections.Counter('hello world'.split())
r2 = collections.Counter('hello albert'.split())
print(r1.update(r2))
print(r1.subtract(r2))


#####################
# defaultdict
d = collections.defaultdict()
e = collections.defaultdict(str)
print(e["hello"])
f = collections.defaultdict(int)
print(f["hello"])
g = collections.defaultdict(list)
print(g["hello"])
h = collections.defaultdict(dict)
print(h["hello"])


#####################
# Orderdict

o = collections.OrderedDict()
o["k1"] = "v1"
o["k3"] = "v3"
o["k2"] = "v2"
print(o)


#######################
# deque
#  collections.deque 队列支持线程安全，对于从两端添加（append）或者弹出（pop），复杂度O(1)。
#  优化了定长操作（pop(0)、insert(0,v)）的开销

d = collections.deque(maxlen=10)
print(d)
d.extend('python')
print(d)
d.append('3')
print(d)
d.appendleft('I')
print(d)
d.appendleft('-')
print(d)
d.append('.')
print(d)
# the first element will be poped from left side, as the queue has reached maxlen
d.append('9')
print(d)
d.popleft()
print(d)
d.pop()
print(d)
d.insert(3, "x")
print(d)
d.remove("x")
print(d)


##########################
# chainmap

d1 = {'apple':1,'banana':2}
d2 = {'orange':2,'apple':3,'pike':1}
combined1 = collections.ChainMap(d1,d2)
combined2 = collections.ChainMap(d2,d1)
print(combined1)
print(combined2)

#ChainMap进行修改的时候总是只会对第一个字典进行修改，如果第一个字典不存在该键，会添加
for k,v in combined1.items():
    # {'apple':3} has been excluded
    print(k,v)

for k,v in combined2.items():
    # {'apple':1} has been excluded
    print(k,v)

# ChainMap 实际上是把放入的字典存储在一个队列中，
# 当进行字典的增加删除等操作只会在第一个字典上进行，
# 当进行查找的时候会依次查找，new_child() 方法实质上是在列表的第一个元素前放入一个字典，默认是{}，
# 而 parents 是去掉了列表开头的元素