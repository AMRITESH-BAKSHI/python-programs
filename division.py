# print(5//-3)
# print(7/-4)
# print("god">"God")
# print(4==4.0)
# l1=[1,2,3,3]

# print(id(l1))
# l1[3]=34
# print(id(l1))
# t1=[1,2,3,3]
# print(id(t1))
# print(l1,t1)
# print(l1==t1)
# print(l1 is t1)
# print(True>False)
# print(ord("4"))

# # question 1
# guessno=7
# userno=int(input("enter the number"))
# print(guessno>=userno)


# f="god"
# h="god"
# print(ord("f"))
# print(ord("h"))
# print(f>=h)
# print(7.2%2.1)
# print(8%3)


# print(0.1+0.1+0.1== 0.3)
# print(0.1+0.1+0.1)
# print(len("30000000000000004"))
# a=1243
# b=1243
# c=b
# print(a is b)
# print(a is c)

# cases when python generate different object with same Value 
#1 when input is taken from the User
s1="av"
s3=input("enter the vale")
print(s1==s3)
print(s1 is s3)
# 2 integers with many digits 
num1=8.239745879236859073894520387523758345235234523452346457645654762252345233245235435645645364232452452345234532453245234523452345235423453
num2=8.239745879236859073894520387523758345235234523452346457645654762252345233245235435645645364232452452345234532453245234523452345235423453
print(num1 is num2)
# print([]>"234")
print(bool([]))
if [] and 3>2:
    print("yuesa")
else:
    print("lol")

print([] and  "")
# even if the second expression will be logically wrong then also it will show true if the first operand is true 
print(20>10 or "aa"+23>1)