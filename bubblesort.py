l=[12,43,654,7856,433,895,34,4536,1212,456,1,2134,2,3,4,5745,1231,6346,12313453,1314,645645,2131,34543,3,2,2,4,78,5,6,1,6]
for c in range(1,len(l)*9+4):
    for i in l:
        if l.index(i)==len(l)-1:
            # print("hello")
            if i<=l[0]:
                k=l.pop(l.index(i))
                l[0]=k
                # print("hello")
        elif i>=l[l.index(i)+1] and l.index(i)!=len(l)-1:
            b=l.pop(l.index(i)+1)
            l.insert(l.index(i),b)
print(len(l))
print(c)
print(l)

