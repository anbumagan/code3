a=str(input())
b=['a','e','i','o','u']
d=0
c=0
for i in range(len(a)):
    if a[i] in b:
        c=c+1 
    else:
        d=d+1
if(c>=1):
    print("yes")
else:
    print("no")
