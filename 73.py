a=int(input())
c,b=input().split()
x=int(c)
y=int(b)
c1=d1=0
for i in range(x+1,y):
    if a==i:
        c1=c1+1
    else:
        d1=d1+1
if(c1>=1):
    print("yes")
else:
    print("no")
