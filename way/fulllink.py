with open(r"A:\python program\web.html","r") as web:
    with open("linkyy.txt","a") as lin:
        for i in web.readlines():
            if "<a href=" in i:
                for b in range(0,len(i)):
                    if i[b:b+8]=="<a href=":
                        fq=b+8
                        sq=i.find("\"",fq+1)
                        lin.write(i[fq+1:sq]+"\n")
