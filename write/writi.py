with open(r"A:\python program\write\file1.txt","r") as f:
    with open(r"A:\python program\write\file2.txt","w") as f2:
        f2.write(f.read())
            
