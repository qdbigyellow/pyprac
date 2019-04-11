from operator import itemgetter
import itertools
import operator 

#groupby只能对连续数据进行分组，因此不能确定数据有序的情况下，建议进行排序操作
rows=[
    {'name':'jim','date':'07/01'},
    {'name':'tom','date':'07/01'},
    {'name':'rose','date':'07/01'},
    {'name':'tom','date':'07/02'},
    {'name':'jim','date':'07/03'},
    {'name':'rose','date':'07/02'},
]

gbrows=sorted(rows,key=operator.itemgetter('date'))
print(gbrows)
for gbdata,row in itertools.groupby(gbrows, key=itemgetter('date')):
    print(gbdata)
    for i in row:
        print(i)

# permutations：按照给定位数对可迭代对象内元素进行组合
print("permutation")
listed = ['a','b','c','d']
for i in itertools.permutations(listed,3):
    print(i)

#combinations：按照给定位数对可迭代对象内元素进行组合，但是结果不重复
print("combination")
for i in itertools.combinations(listed, 3):
    print(i)

# combinations_with_replacement：与combinations区别就是同一元素可以使用多次
print("combination with replacement")
for i in itertools.combinations_with_replacement(listed, 3):
    print(i)

#zip_longest：对多个数据按索引进行组合,并根据迭代对象的大小，不足使用fillvalue默认值替代
a=[1,2,3]
b=['a','b']
print("zip_longest")
for i in itertools.zip_longest(a,b,fillvalue="nihao"):
    print(i)
    
print("normal zip") 
for i in zip(a,b):
    print(i)    

print("dropwhile")
# dropwhile:对可迭代对象的元素依次进行函数过滤，遇到返回False的元素就停止
listed=[-1,0,-3,2,-5,4,2]
for i in itertools.dropwhile(lambda s:s<3,listed):
    print(i)


print("product")
#product：可以说是combinations的升级版，对多个序列进行组合，且无重复
list1=[1,2,3]
list2=[4,5]
list3=['a']

for i in itertools.product(list1,list2,list3):
    print(i)

#islice:对迭代器，可迭代对象进行切片操作
iter=(i for i in range(10))
for i in itertools.islice(iter,0,10,2):
    print(i)

#chain:对多个可迭代对象进行组合
list1=[1,2,3]
set1={'a','b'}

for i in itertools.chain(list1,set1):
    print(i)