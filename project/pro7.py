# hollow triangle
a="* "
n=int(input("enter the number"))
b=n-1
for i in range(1,n+1):
    if i==n:
        print(a*n)
    elif i==1 or i==2:
        print(b*" "+a*i)
    elif i>2 and i<n:
        print(b*" "+a+(i-2)*"  "+a)
    b-=1
    