# reverse the order of the string inside list
l1=list(input('enter the word to be reversed').split(','))
reversedlist=[]
for i in l1:
    reversedlist.append(i[-1::-1])
print(reversedlist)
