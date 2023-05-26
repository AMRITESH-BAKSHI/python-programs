user=input('''select the option
(a)print the length of the shortest string in the lists of string 
(b)print new list where each element is sum of corresponding element
''')

if user.lower()=='a':
    strslists=list(input("enter the lists of string comma separated").split(","))
    maxlength=len(strslists[0])
    for i in strslists:
        if len(i)>maxlength:
            items=i
            maxlength=len(i)
    print("the longest character is of length",maxlength)
elif user.lower()=='b':
    num=int(input("enter the num"))
    listofnum=[1,2,3,4,5]
    listsnew=[]
    for i in listofnum:
        listsnew.append(i+num)
    print(listsnew)


