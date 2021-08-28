n = int(input("Width : "))

for i in range(1,n+1):
    if(i == 1): #TOP
        print(i)
    elif(i == n): #Bottom
        for j in range(0,n):
            print(i,end="")
    else : # Between Top and Bottom
        for j in range(0,i):
            if(j == 0 or j == (i-1)):
                print(i,end="")
            else : print(" ",end="")
        print("")