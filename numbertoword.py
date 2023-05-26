l1=[" ","one ","two ","three ","four ","five ","six ","seven ","eight ","nine "]
l2=[" ","ten ","twenty ","thirty ","fourty ","fifty ","sixty ","seventy ","eighty ","ninety "]
# l3=[" ","crore","lakh ","thousands ","hundred "]
l3=["hundred ","thousands ","lakhs ","crore "]
l4=["eleven ","twelve ","thirteen ","forteen ","fifteen ",'sixteen ',"seventeen ","eighteen ","nineteen "]

n=int(input("enter the number"))
word=""
# if len(str(n))%3==0:
num=str(n)
b=int(len(num)/3) +1
num2=num[0:b+1]
c=int(len(num)/2)+1
l6=l3[0:c-1]
l6.reverse()
l6.insert(0," ")
print(l6)

for i in range(0,b,2):
    word+= l6[i]+l1[int(num2[0])]+l6[i+1]+l2[int(num2[1])]+l1[int(num2[2])]
    num2=num[b:b+3]

print(word)




        




    

