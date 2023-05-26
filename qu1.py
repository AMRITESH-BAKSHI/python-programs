a=[12,124,124,1312,-1,124,-234]
mins=a[0]
for i in a:
    if i<mins:
        mins=i


print(mins)
print(a.index(mins))
