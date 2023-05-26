import math
x=int(input("enter the value"))
n=int(input("enter the number of terms "))
answer=0
for i in range(1,n+1):
    answer+=math.pow(x,i)/i
print(answer)
