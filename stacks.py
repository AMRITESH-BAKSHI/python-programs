stack=[]
def push(element):
     stack.append(element)
def pops(st):
     if st:
          d=st.pop()
          return d 
     else:
          print("stack underflow")
def peek(st):
     return st[len(st)-1]
def displaystack(st):
     if st:
          for i in st:
               print(i)
     else:
          print('stackempty')
#stack=[]
while True:
     c=input("""choose the value
             1->push
             2-->pop
             3-->display
             4-->peek
             5->exit
             ente the choice: """)
     if c=="1":
          val=input("enter the value to push")
          push(val)
     elif c=="2":
          if len(stack)==0:
               print("underflow condition")
          else:
               pops(stack)
     elif c=="3":
          if len(stack)==0:
               print("no data in stack")
          else:
               displaystack(stack)
     elif c=="4":
          if len(stack)==0:
               print("underflow condition")
          else:
               print(peek(stack))
     else:
          break
          
          
          
     
