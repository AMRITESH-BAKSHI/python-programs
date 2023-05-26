# a=12
# b=23
# c=242
# if a>b and a>c:
#     print(a)
# if b>c and b>a:
#     print(b)
# if c>a and c>b:
#     print(c)
# # method2
# maxs=a
# if b>maxs:
#     maxs=b
# if c>maxs:
#     maxs=c
# print(maxs)
# # method3
# l=[a,b,c]
# print(max(a,b,c))

#####################################
a=2
b=2
c=132
sums=0
if a==b and b==c:
    print(sums)
elif a==b :
    sums+=c
    print(sums)
elif b==c:
    sums+=a
    print(sums)
elif a==c:
    sums+=b
    print(sums)
elif a!=b and b!=c:
    sums+=a+b+c
    print(sums)

# method 2
sums1=0
if a!=b and a!=c:
    sums1+=a
elif b!=a and b!=c:
    sums1+=b
elif c!=a and c!=b:
    sums1+=c
else:
    print("d")
print(sums1)
# /////////////////
a=3
b=34
c=12
d=42
l1=[a,b,c,d]
counts=0
divisor=3
for i in l1:
    if i%divisor==0:
        counts+=1   
print("multiples found ",counts)
# ......................................
a=234
b=2
c=323423
# l1=[a,b,c]
# l1.sort()
# print(l1)

# /////////////////
l=[]
if a<b and a<c:
    l.append(a)
    if b>c:
        l.append(c)
        l.append(b)
    else:
        l.append(c)
if b<c and  b<a:
    l.append(b)
    if a>c:
        l.append(c)
        l.append(a)
    else:
        l.append(a)
        l.append(c)
if c<a and c<b:
    l.append(c)
    if a>b:
        l.append(b)
        l.append(a)
    else:
        l.append(a)
        l.append(b)
print(l)
        # //////////////
print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("B"))
print(ord("1"))
print(ord("2"))

ch=input("enter the anything ")
if ch>="A" and ch<="Z":
    print('the character is uppercase')
elif ch>="a" and ch<="z":
    print('the character is lowercase')
elif ch>="1" and ch<="9":
    print("you entered the digit")
else:
    print("you entered special characker")

#/////////////////////////////////////
absent_students=["amritesh","abhinav","himanshu","aditya"]
if "amritesh" in absent_students:
    print("give message to amritesh parensts that he is absent  ")
if "asdf" not in absent_students:
    print("heelo")

# /////////////////////////////////
a=12
while a<100:
    print("you are duffer")
    b=23
    # print345)
    a+=1
a=4
fact=1
while a!=0 :
    fact*=(a)
    a-=1

print(fact)
# ?/////////////////
n=10
eve=0
odd=0
while n!=0:
    if n%2==0:
        eve+=n
    else:
        odd+=n
    n-=1

print(eve)
print(odd)










