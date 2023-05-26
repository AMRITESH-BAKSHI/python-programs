userpass=input("enter the passsword")
l=["1","2","3","4","5","6","7","8","9","0"]
if userpass[0] in l  and len(userpass)>=6:
    print("password accepted")
else:
    print("password is wrong")
