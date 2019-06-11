a,b=map(int,input().split())
c=list(map(int,input().split()))
l=[]
for i in c:
    if(i%2!=0):
        l.append(i)
print(l[b-1])
