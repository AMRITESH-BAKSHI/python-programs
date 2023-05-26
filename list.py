# sl1=l1[5:15:2]
# sl2=l1[::4]
# print(sum(sl1))
# print(sum(sl2))
# l2=[1,23,34]
# l2.append(232)
# print(l2)
from copy import copy


l1=[1,2,3,4,5,6,7,8,22,9,10,11,12,13,14,15,16,17,18,19,20]
# del l1[8]
l1.pop(8)
print(l1)
# to make true copy
a=[1,2,3]
b=list(a)
a[1]=234
print(a)
print(b) 

print(l1.index(12))
l1.extend([1,123,123])
print(l1)
print(l1.extend([1,123,123]))

l1.insert(11,"saitama")
l1.remove(1)
print(l1)
l1.reverse()
print(l1)

