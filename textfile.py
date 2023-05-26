import os
a=open("text.txt","r")
temp=open("temp.txt","w")
'''
while True:
     name=input("enter the name: ")
     contactnumber=int(input("enter the number"))
     dc={"name":name,"contact number":contactnumber}
     a.write(str(dc)+"\n")
     ch=input("enter the choice y or no")
     if ch=="n" or ch=="no":
          break
     else:
          continue
   '''

c=a.readlines()
for i in c:
     c=eval(i)
     if c["name"]=="amritesh":
          c["name"]="ramji"
          temp.write(str(c)+"\n")
     else:
          temp.write(str(c)+"\n")
temp.close()
a.close()
os.remove("text.txt")
os.rename("temp.txt","text.txt")

     
     
