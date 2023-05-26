import pickle as p
with open("a.dat","rb+") as f:
     #p.dump({"name":"animesh bakshi","class":"5","favourite anime":"dragon ball z , spy x family , naruto,onepunchman, shinchan"},f)
     found=False
     try:
          while True:
               rpos=f.tell()
               data=p.load(f)
               if data["name"]=="animesh":
                    data['class']="4"
                    f.seek(rpos)
                    p.dump(data,f)
                    found=True
     except :
          if found==True:
               print("successfully updated")
          else:
               print("not found")
          f.closed
               
     
