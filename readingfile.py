f=open("file.txt","r")
# print(f.tell())
# print(f.read()) 
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read())
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")
# lines=f.readlines()
# print(lines,len(lines))
for line in f.readlines()[:5]:
    print(line,end="")
print(f.name)
f.close()
print(f.closed)

















f.close()