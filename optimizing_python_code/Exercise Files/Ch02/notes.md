**bict**
https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html

http://kuanghy.github.io/2016/06/14/python-bisect
Python 有一个 bisect 模块，用于维护有序列表。bisect 模块实现了一个算法用于插入元素到有序列表。在一些情况下，这比反复排序列表或构造一个大的列表再排序的效率更高。Bisect 是二分法的意思，这里使用二分法来排序，它会将一个元素插入到一个有序列表的合适位置，这使得不需要每次调用 sort 的方式维护有序列表。

**deque**
Deque是一个queue，但是可以从两头任意写入和读出。

**heapq**
prioirity queue, 每一个task都有priority
prioity 1 > prioirty 3

**scipy.spatial.KDTree**
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.html

如果有任何performance的问题，考虑使用第三方的数据结构，可能会提升性能。