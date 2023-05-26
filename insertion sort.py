a=[435,1,245,1,5]
print(a)
for i in range(len(a)-1):
     for c in range(0,i):
          if a[c]<a[i]:
               print()
               a[c+1]=a[i]
          elif a[c]>a[i]:
               a[c-1]=a[i]
          else:
               pass
print(a)
     
