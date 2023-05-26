name=input("enter your name")
print("WELCOME TO COVID DETECTOR PORTAL",name)
counter=0
evidence=[]
ques1=input("DID YOU WENT TO ABROAD RECENTLY")
if ques1=="yes":
    evidence.append("abroad")
    counter+=1
ques2=input(""" WHAT SYMPTOMS DO YOU HAVE  
1-COUGH  
2-HIGH FEVER  
3-MILD FEVER  
4-NO FEVER
5-BREATHING PROBLEM 
6-PAIN in HEART
 """).lower().split(",")
evidence.extend(list(ques2))
counter+=len(ques2)
ques3=input("""you live in which area 
1-Red zone
2-yellow zone
3-green zone
""").lower()
evidence.append(ques3)
if ques3!="green zone":
    counter+=1
if counter<3 and "red zone" not in evidence :
    print("you seems fine but take some rest ")
    print("please always wear mask and smile")
elif counter>2 and counter<4 and"red zone" in evidence or "pain in heart" in evidence:
    print("we recommend you to consult a doctor ")
elif counter>=4 and("red zone" in evidence or"yellow zone" in evidence)and "high fever"in evidence and"breathing problem"in evidence:
    print("please give the covid test and remain in isolated area of your house ")
