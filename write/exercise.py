with open(r"A:\python program\write\file1.txt","r") as salary:
    for i in salary.readlines():
        name,salary=i.split(",")
        with open("salary.txt","r+") as sal:
            sal.seek(len(sal.read()))
            sal.write(name+"'s"+" salary is "+salary)

