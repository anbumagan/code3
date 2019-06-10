a6=int(input())
c=0
for i in range(2,a6):
    if((a6%i)==0):
        c=1
if(c==0):
    print("yes")
else:
    print("no")
