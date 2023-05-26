# onlinehotelbooking
print("hello welcome to the hotel")
cost=0
username=input("whats your good name")
age=input("whats your age ")
adcardnum=int(input("enter you addhar card number"))
address=input("whats yours address")
print("ok well")
Userask=input("do you want a room or suite").lower()
if Userask=="room":
    room=input("""which room would you like to take sir
    1->SINGLE ROOM  ,PRICE->1200RS FOR 24HOURS
    2->DOUBLE ROOM  ,PRICE->1500RS FOR 24HOURS
    2->KING ROOM  ,PRICE->4000RS FOR 24HOURS
    """).lower()   
    if room=="single room" or room=="1":
        room="single room"
        cost=1200
    elif room=="double room" or room=="2":
        room="double room"
        cost=1500

    elif room=="king room" or room=="3":
        room="king room"
        cost=4000

elif Userask=="suite":
    room=input("""which suit would you like to take sir
    1->MASTER SUITE ,PRICE->6000 RS FOR 24HOURS
    2->JUNIOR SUITE ,PRICE->7000 RS FOR 24HOURS
    """).lower()
    if room=="master suite" or room=="1":
        room="master suite"
        cost=6000
    elif room=="junior suite" or room=="2":
        room="junior suite"
        cost=7000

days=int(input("FOR HOW MANY DAYS YOU WANT TO STAY"))
if days<3:
    print(F"""well,so you are {username} of age {age}
     YOUR CREDENTIALS ARE- 
    ADDHAR CARD NUMBER--> {adcardnum}
    ADDRESS--> {address} 
    you took {room}
    total days-->{days}
    payment to be made on checkout date -->{cost*days}
    """)
elif days>=4:
    discountcost=(90/100)* (cost*days)
    print(F"""well,so you are {username} of age {age}
     YOUR CREDENTIALS ARE- 
    ADDHAR CARD NUMBER--> {adcardnum}
    ADDRESS--> {address} 
    you took {room}
    total days-->{days}
    payment to be made on checkout date -->{discountcost}
    """)
