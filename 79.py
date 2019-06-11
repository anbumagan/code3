import math
a,b=input().split()
x=int(a)
y=int(b)
z=x*y 
if(math.sqrt(z)==x or math.sqrt(z)==y):
    print("yes")
else:
    print("no")
