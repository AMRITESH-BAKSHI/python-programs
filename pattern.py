l1=["A ","B ","C ","D ","E ","F "]
final=""
for i in range(0,6):
    final+=l1[i]
    print(final)

# q2
for i in range(0,5):
    print((i+1)*l1[i],sep=" ")
# q3
c=" "
d=0
print(0)
for i in range(1,5):
    for b in range(0,6):
        b=d+2
        c=str(b)*i
        print(c)
        d=b
        break
# method 2 for q3
# l3=[]
# for i in range(0,10,2):
#     l3[0]=i
# for b in range


