def enqueue(qu,i):
     qu.append(i)
def dequeue(qu):
     d=qu.pop(0)
     return d
def peek(qu):
     return qu[0]
def display(qu):
     for i in qu:
          print(i)
def cls():
     print("\n"*100)
queue=[]
while True:
     ch=input("""chose the options
               1-->enqueue
               2-->dequeue
               3-->peek
               4-->display
               5--->clear screen
               6-->exit
               enter the choice:""")
     if ch=="1":
          data=input("enter the data to  the queue")
          enqueue(queue,data)
     elif ch=="2":
          if len(queue)==0:
               print("queue underflowed")
          else:
               print("dequeue data is ",dequeue(queue))
     elif ch=="3":
          if len(queue)==0:
               print("queue underflowed")
          else:
               print(peek(queue))
     elif ch=="4":
          if len(queue)==0:
               print("queue underflowed no data present")
          else:
               display(queue)
     elif ch=="5":
          cls()
     elif ch=="6":
          break
     else:
          print("please give valid input")
               
          

