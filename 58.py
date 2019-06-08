a,b=input().split()
x=int(a)
y=int(b)
s=list(map(int,input().split()))
for i in range(len(s)):
    if(s[i]==y):
        print("yes")
        break
    else:
        print("no")
        break
