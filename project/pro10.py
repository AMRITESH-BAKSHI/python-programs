lists=["ONEPUNCHMAN",'SAITAMA','GOKU','VEGETA']
fst3let=[]
remaining=[]
new=[]
for i in lists:
    b=i[3:]
    fst3let.append(i[0:3])
    remaining.append(b)
c=0
remaining.reverse()
for i in remaining:
    new.append(fst3let[c]+i)
    c+=1
print("original",lists)
print("new",new)


