import random
num=random.randint(1,101)
print(num)
if num%3==0 and num%5!=0:
    print("fizz")
elif num%5==0 and num%3!=0:
    print("buzz")
elif num%5==0 and num%3==0:
    print("fizzbuzz")
else:
    print("no")
