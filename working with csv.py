import csv as c
a=open("file.csv","r+",newline="\r\n")

a.seek(0)
'''
f=c.writer(a,delimiter=",")
f.writerow(["name","class","anime"])
while True:
     name=input("enter your name")
     clas=input("enter your class")
     anime=input("enter your favourite anime")
     ask=input("wanna enter more info y/n")
     f.writerow([name,clas,anime])
     a.flush()
     if ask.lower()=="y" or ask.lower()=="yes":
          continue
     else:

          break
'''
r=c.reader(a)
print(list(r))
#print(list(r))
#print(list(r))
for i in r:
     print(i)

a.flush()
a.close()
