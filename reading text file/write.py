# w , a ,r+
# for append
# with open("ok.txt","a") as note:
#     note.write(" \n skillet monster")
# r+
# do not create the newfile
with open("file4.txt","r+") as f:
    f.seek(len(f.read()))
    f.write("hell this isissfs")
    print(f.read())