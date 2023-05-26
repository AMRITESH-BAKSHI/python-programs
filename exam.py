# user=input(""" 
# a--> maximum length of the string from the given list
# b--> summed the corresponding number of list with number entered by user
#  """)
# if user=="a":
#     str_list=["Onepunchman","exam","saitama","dragon ball z","mob psyco"]
#     num=[]
#     for i in str_list:
#         num.append(len(i))

#     a=max(num)
#     b=num.index(a)
#     print(str_list[b])

# elif user=="b":
#     num=int(input("enter the number"))
#     l=[1,2,3,4]
#     v=[]
#     for k in l:
#         v.append(k+num)
#     print(v)


# it was simple man
string=input("enter alphanumeric string")
b=[]
for i in string:
    if i.isdigit():
        b.append(int(i))
    
if len(b)==0:
    print("the string has no integer")
else:
    print("original string is ",string)
    print("the digits are",b)
    print("the sum of digits are ",sum(b))









