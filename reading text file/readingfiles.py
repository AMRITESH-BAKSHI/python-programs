f=open(r"A:\python program\reading text file\file.txt","r") #by default read mode
# use r for specifying the name of the path 
# windows - \n \t are escape sequences
print(f.read())


f.close()