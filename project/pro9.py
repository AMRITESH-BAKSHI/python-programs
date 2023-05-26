user=input('enter the string')
collectednum=[]
sums=0
for i in user:
    if i.isnumeric():
        collectednum.append(int(i))

if collectednum:
    print(collectednum,"sum is ",sum(collectednum),"in original string",user)
else:
    print("string",user,"has no digit")
    
