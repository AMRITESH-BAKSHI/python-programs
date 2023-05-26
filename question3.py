import os
from functionss import *
while True:
    os.system("cls")
    a=input("""choose any program:
    1->for prime number
    2->for armstrong number
    3->for perfect number
    4->fibonacci number
    5->for exit
    """)
    if a=="1":
        primenum()
    elif a=="2":
        armstrngnum() 
    elif a=="3":
        prfectnum()
    elif a=="4":    
        fibonaciseries()  
    elif a=="5":
        print("thanks for using software come back later")
        input("press any key to continue")
        break


