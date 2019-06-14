a=str(input())
a1=a.replace(" ","")
a2=[]
for i in a1:
    if(a1.count(i)==1):
        a2.append(i)
print(*a2,end=" ")
