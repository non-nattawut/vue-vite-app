while(True):
    line = int(input("Enter an odd base (3-9) : "))
    if(line%2 == 0 or line < 3 or line > 9):
        print("Invalid Number!!!")
        print("The number must be an odd number from 3 to 9.")
    else: break

MaxRow = line//2 + 1

for i in range(1,line+1):
    print("Row %d -> "%i,end="")
    if(i > MaxRow):
        for j in range(1,MaxRow):
            print(i,end="")
        MaxRow -= 1
    else :
        for j in range(1,i+1):
            print(i,end="")
    print("")
        