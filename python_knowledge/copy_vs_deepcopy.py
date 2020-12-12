import copy

l1 = [1, 2, 3]
l2 = l1
l3 = copy.copy(l1)

print(f"original {id(l1)}")
print(f"l1 is mutable, so assign l2 = l1, making l2 has the same id as l1, {id(l2)}")
print(f"l1 is mutable, so copy l3 from l1 will create a new object.  {id(l3)}")

l1[0] = 11

print(l1)
print(f"after change a value in mutalbe, still has the same object {id(l1)}")
print(l2)
print(f"l2 has the same value as l1. because it references to the same space. {id(l2)}")
print(l3)
print(f"l3 still has the original value, as it has its own space {id(l3)}")


a = [4, 5]
l1 = [1, 2, 3, a]
l2 = l1
l3 = copy.copy(l1)
l4 = copy.deepcopy(l1)

print(f"a is a mutable, {id(a)}")
print(f"original l1 which contains another mutable a: {id(l1)}")
print(f"l1 is mutable, so assign l2 = l1, making l2 has the same id as l1, {id(l2)}")
print(f"l1 is mutable, so copy l3 from l1 will create a new object.  {id(l3)}")
print(f"l1 is mutable, so deepcopy l4 from l1 will create a new object.  {id(l4)}")

a[0] = 14

print(a)
print(f"{id(a)}")
print(l1)
print(id(l1))
print(l2)
print(id(l2))
print(l3)
print(f"Because copy only copy a reference, so if there is a mutable obj A in a mutalble obj B,  \
      and the value in A is changed, the copied value in B will be changed too.  {id(l3)}")
print("")
print(l4)
print(f"In this case, deepcopy also make copy for mutable in mutable, so if there is a mutable obj A in a mutalble obj B,  \
      and the value in A is changed, the copied value in B will NOT be change. {id(l4)}")
