def primenum():
    print("PRIME NUMBER IDENTIFIER")
    b=int(input("enter the number "))
    c=0
    for i in range(2,(b//2)+1):
        if b%i==0:
            c+=1
    if c!=0:
        print(b,"is not prime")
    else:
        print(b,"is prime number")
    input("press any key to continue")
def armstrngnum():
    print("ARMSTRONG NUMBER IDENTIFIER")
    b=int(input("enter the number"))
    total=0
    for i in str(b):
        total+=int(i)**len(str(b))
    if total==b:
        print(b,"is armstrong number ")
    else:
        print(b,"is not armstrong number")
    input("press any key to continue")
def prfectnum():
    print("PERFECT NUMBER IDENTIFIER")
    b=int(input("enter the number"))
    total=0
    for i in range(1,b//2+1):
        if b%i==0:
            total+=i
    if total==b:
        print(total,"is a perfect number")
    else:
        print(b," is not a perfect number")
    input("press any key to continue")
def fibonaciseries():
    print("FIBONACCI SERIES")
    b=int(input("enter the number"))
    s=0
    t=1
    print(s,end=" ")
    print(t,end=" ")
    for i in range(1,b):
        c=s+t
        print(c,end=" ")
        s=t
        t=c 
    #print()
    input("press any key to continue")
    