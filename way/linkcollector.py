with open(r"A:\python program\web.html","r") as links:
    for i in links.readlines():
        # if "a href=" in i:
        #     c=[]
        #     for b in range(0,len(i)):
        #         if i[b]=='"':
        #             c.append(b)
        #     print(c)
        #     with open("linkss.txt","r+") as lin:
        #         a=i[c[0]+1:c[1]]+"\n"
        #         lin.seek(len(lin.read()))
        #         lin.write(a)
        if "<a href=" in i:
            pos=i.find("<a href=")
            i=i+"\n"        

            firstquote=i.find("\"",pos)
            secondquote=i.find("\"",firstquote+1)
            with open("linkss.txt","r+") as lins:
                lins.seek(len(lins.read())) 
                lins.write(i[firstquote+1:secondquote]+"\n")


                
