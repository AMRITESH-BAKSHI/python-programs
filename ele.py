election={"amritesh":23,"nilesh":54,"himanshu":45}
l1=[]
l2=[]
for i,j in election.items():
    l1.append(i)
    l2.append(j)

l2.sort(reverse=True)
for i in l2:
    for b in l1:
        if (b,i) in election.items():
            print(b,i)


        
