n=int(input("enter the number"))
fib=[0,1]
a=0
b=1
for i in range(n):
    s=a+b
    fib.append(s)
    a=b
    b=s
print(fib[n])