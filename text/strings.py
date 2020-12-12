

# use negative index and step length to reverse the string
str1 = "qwert"
rev_str1 = str1[::-1]
print(rev_str1)

# .title() to select first letter of each word
str1="this is a book" 
print(str1.title()) 

# use set to filter the unique element in the string
str1="aabbccccdddd"
set1=set(str1) 
new_str=''.join(set1) 
print(new_str)

#  use * to repetitive the string or list
i=4 
str1="abcd" 
list1=[1,2] 
print(str1*i) 
print(list1*i) 

# use collectoins.Counter() to check the number of appearance
from collections import Counter
list1=['a','b','a','c','c','c']
count=Counter(list1)
print(count)
print(count['b'])
print(count.most_common(1))

# use enumerate to get the index of list

list1=['a','b','c','d','e']
for idx,val in enumerate(list1):
  print('{0}:{1}'.format(idx,val))
  

# use getsizeof to check the memory usage of a variable
import sys
num=21
print(sys.getsizeof(num))


# from iteration_utilities import deepflatten
# 如果嵌套列表的深度只有1层
def flatten(l):
      return [item for sublist in l for item in sublist]
l=[[1,2,3],[3]]
print(flatten(l))
# [1,2,3,3]

# 如果不知道列表嵌套深度
## deepflatten to iterate multi-dimension list
## l=[[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]
## print(list(deepflatten(l,depth=3)))
# [1,2,3,4,5,6,7,8,9,10]

# use map to convert intger to a integer list
# map(func, iter)
nums=123456
# 使用map
digit_list=list(map(int,str(nums)))
print(digit_list)
# [1,2,3,4,5,6]
# 使用列表表达式
digit_list=[int(x) for x in str(nums)]
print(digit_list)
# [1,2,3,4,5,6]
