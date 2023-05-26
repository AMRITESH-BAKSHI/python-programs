a="* "
n=int(input("enter the length of triangle"))
b=n-1
for i in range(1,n+1):
    print(b*' '+i*a)
    b-=1
