a=str(input())
b2=list(a)
for i in b2:
    if(i.isnumeric()):
        print(i,end="")
    else:
        print("")
