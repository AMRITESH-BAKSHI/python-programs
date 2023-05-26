a="* "
d=2
for q in range(1,4):
    for b in range(d+1):
        v=" "*d+q*a
    print(v)
    d-=1
d=1
c=0
for q in range(2,0,-1):
    for b  in range(d):
        c=" "*d+q*a
    d+=1
    print(c)


