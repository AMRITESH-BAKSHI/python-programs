a=[2,1,4,67456456,445,3,5,1]
print(a)
for g in range(len(a)):
     for i in range(0,len(a)-g-1):
          if a[i]>a[i+1]:
               c=a[i+1]
               a[i+1]=a[i]
               a[i]=c
print(a)
