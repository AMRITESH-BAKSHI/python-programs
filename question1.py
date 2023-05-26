sentence=input("enter the sentence")
sentwthoutspace=" "+sentence.strip(" ") 
digits=0
alpha=0
space=0
specha=0
word=0
specia=[]
for i in range(0,len(sentence)):
    if sentence[i].isalpha():
        alpha+=1
    elif sentence[i].isdigit():
        digits+=1
    elif sentence[i].isspace():
        space+=1
    else:
        specha+=1
        specia.append(sentence[i])
for b in range(0,len(sentwthoutspace)):
    if sentwthoutspace[b]==" " and sentwthoutspace[b-1]!=" " and sentwthoutspace[b-1] not in specia and sentwthoutspace[b-2] not in specia:
        word+=1
print(digits,alpha,space,specha,word)
