'''for i in range(1,5):
    print(i)
    if i==4:
        break
else:
    print("loop terminated normally")
# q1
sums=0
counts=0
ans='y'
while ans!="n":
    a=int(input("enter the number"))
    sums+=a
    counts+=1
    ans=input("want to enter more number y or n")
    if ans=="y":
        continue
else:    
    print('you enterd ',counts ,"so far")
    print("sum of numbers so far is ",sums)

# /////////////////////////////
a=45
li=[]
for i in range(1,46):
    if 45%i==0:
        li+=[i]
if len(li)>2:
    print(a,"it  is not prime")
else:
    print(a,"is prime")

'''
# 








# a=int(input("enter the number "))
# b=2
# print(a/b)



a=0
b=1
final="0"
for i in range(1):
    final+=" "+str(a+b)
    b=a+b
    a,b=b,a
print(final)

a=5
b=4
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        hcf=i

print(hcf)
a=0
b=0
c=0
for i in range(1,7):
    for b in range(0,i+1):
        c+=b




print(c)


                                                   

