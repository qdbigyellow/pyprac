# nlargest(n, iterable, key=None)
# nsmallest(n, iterable, key=None)
#n:查找个数    iterable:可迭代对象    key：同sorted

# 使用用于返回 n个最大值，或者n个最小值的情形。 
from operator import itemgetter
import heapq


list1=[1,6,4,3,9,5]
list2=['12','a6','4','c34','b9','5']
list3=[
    {'name':'jim','age':23,'price':500},
    {'name':'mase','age':23,'price':600},
    {'name':'tom','age':25,'price':2000},
    {'name':'alice','age':22,'price':300},
    {'name':'rose','age':21,'price':2400},
]

print(heapq.nlargest(len(list1),list1))
print(heapq.nlargest(len(list2),list2))
print(heapq.nlargest(len(list3),list3,key=itemgetter('age','price')))

#以上代码输出结果同sorted

print(heapq.nsmallest(len(list1),list1))
print(heapq.nsmallest(len(list2),list2))
print(heapq.nsmallest(len(list3),list3,key=itemgetter('age','price')))
#结果是降序
# [1, 3, 4, 5, 6, 9]
# ['12', '4', '5', 'a6', 'b9', 'c34']
# [{'name': 'rose', 'age': 21, 'price': 2400}, {'name': 'alice', 'age': 22, 'price': 300}, {'name': 'jim', 'age': 23, 'price': 500}, {'name': 'mase', 'age': 23, 'price': 600}, {'name': 'tom', 'age': 25, 'price': 2000}]
# heappush,heappop,heapify,heapreplace,heappushpop
# 堆结构特点：heap[0]永远是最小的元素(利用此特性排序)

# heapify：对序列进行堆排序，
# heappush:在堆序列中添加值
# heappop:删除最小值并返回
# heappushpop:添加并删除堆中最小值且返回，添加之后删除
# heapreplace:添加并删除队中最小值且返回，删除之后添加

nums=[54,23,64,323,53,3,212,453,65]
heapq.heapify(nums)    #先进行堆排序, 把list变成一个heap
print(nums)
print(heapq.heappop(nums))    #3
print(heapq.heappush(nums,50))    #添加操作，返回None
print(nums)
print(heapq.heappushpop(nums,10))    #由于是添加(push)后删除(pop)，所以返回10. 等于先把10 push，然后在pop 10，因为10是最小的。 
print(heapq.heappop(nums))    #23
print(heapq.heapreplace(nums,10))    #和heappushpop相反，先pop在push，返回50， 
print(nums)    #[10, 53, 54, 65, 323, 64.0, 212, 453]