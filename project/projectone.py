# password changer
interface=input("""DO YOU WANT TO CHANGE YOUR PASSWORD YES OR NO  """)
renew=True
if interface.upper().strip()=="YES":
    while renew==True:
        newpass=input("ENTER THE NEW PASSWORD ") 
        while True:
            confirmpass=input("CONFIRM PASSWORD")
            if newpass==confirmpass:
                print("your password is successfully changed")
                renew=False
                break
            else:
                print("please enter correct password")
                renew=input("do you want to change password again ")
                if renew=="yes":
                    renew=True
                    break
                continue    
else:
    print("thanks for coming")
