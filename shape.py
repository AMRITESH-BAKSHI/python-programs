x="* "
y=" "
d=0
h=1
for i in range(2,-1,-1):
    for b in range(1,4):
        b=d+1
        d=b
        print(y*i+x*b)
        break

    
c=1
for i in range(1,3):
    for b in range(0,1):
        b=c+1
        c=b
        if b>=3:
            print(y*2+x*1)
        else:
            print(y*i+x*b)
            break




