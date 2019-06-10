z=int(input())
while(z>0):
    if(z&(z-1)):
        z=z+1
    else:
        print(z)
        break
