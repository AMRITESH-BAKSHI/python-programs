name=input('enter the name ')
lists=[]
count=0
for i in name:
    count=0
    for b in name:
        if i in lists:
            pass
        else:
            if b==i :
                count+=1
    if i not in lists:
        print(i,count)
    lists.append(i)
