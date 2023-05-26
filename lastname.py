l=[("amritesh bakshi","computer",1937),("Ronald Ross","medicine",),("Marie curie","physics",1954)]
k=[]
for i in l:
    c=i[0].index(" ")
    v=i[0][c+1::1]
    k.append(v)
k.sort()
s=[]
print(k)
for c in k:
    for b in l:
        if c in b[0]:
            s.append(b)
        
print(s)



