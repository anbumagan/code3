l=list(map(int,input()))
c=0
d=0
for i in l:
    if(i==0 or i==1):
        c=c+1
    else:
        d=d+1
if(c>=1):
    print("yes")
else:
    print("no")
