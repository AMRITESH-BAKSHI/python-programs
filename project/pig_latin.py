userwants=input("""which conversion you want
1- normal text to pig latin language 
2- pig latin to normal text
"""
)
if userwants=="1":
    l1=input("enter normal text  to convert into pig latin").split(",")
    l2=[]
    for i in l1:
        final=i[1:]+i[0]
        l2.append(final+"ay")
    print(l2)
# for reverse
elif userwants=="2":
    l3=input("enter pig latin text to convert into normal text").split(",")
    l4=[]
    for i in l3:
        k=i.replace("ay"," ").strip()
        lst=k[-1]
        final=k.replace(lst," ").strip()
        l4.append(lst+final)
    print(l4)
else:
    print("sorry we dont understand")
