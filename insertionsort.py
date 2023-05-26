# l=[5,3,9,6,5,1,10,8,2,7,12,23,25252,21,23123,13]
# for k in range(1,len(l)+1):
#     for i in l :
#         for b in l[0:l.index(i)+1]:
#             if b >i and b!=i:
#                 g=l.pop(l.index(i))
#                 l.insert(l.index(b),g)
#             elif b==i:
#                 h=l.index(b)
#                 g=l.pop(l.index(i,h+1))
#                 l.insert(h,g)

# print(l)
# print(k)
# print(len(l))

# method 2 
l=[5,3,9,6,5,1,10,8,2,7,12,23,25252,21,23123,13]
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=key
print(l)