n = int(input("Width : "))

for i in range(0,n):
    if(i == 0 or i == (n-1)):
        """top and bottom"""
        for j in range(0,n):
            print("*",end="")
        print("")
    else:
        """Between top and bottom"""
        for j in range(0,n):
            if(j == 0 or j == (n-1)):
                print("*",end="")
            else:
                print(" ",end="")
        print("")