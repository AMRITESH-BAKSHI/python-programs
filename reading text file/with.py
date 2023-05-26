with open(r"A:\python program\file.txt") as f:
    a=f.read()
    print(a[:100])
    
print(f.closed)