a=str(input())
a1=a.replace(" ","")
x=a1.lower()
a2=[]
for i in x:
    if(x.count(i)==1):
        a2.append(i)
print(*a2,end=" ")     
        
