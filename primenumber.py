a=int(input("enter the number"))
c=0
d=[]
for i in range(1,(a//2)+1):
     if a%i==0:
          d.append(i)
          c+=1
if a==2:
     print("num is prime",a)
elif c==1:
     print("num is  prime",a)
else:
     print("num not prime",a,d)
     
