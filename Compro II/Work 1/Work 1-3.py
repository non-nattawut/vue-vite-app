while(True):
    line = int(input("Enter an odd base (3-9) : "))
    if(line%2 == 0):
        print("Invalid Number!!!")
        print("The number must be an odd number from 3 to 9.")
    else: break

line = line//2 + 1 #จำนวนบรรทัด
startRow = endRow = line

for i in range(0,line):
    print("Row %d ->  "%i,end="")
    for j in range(0,startRow-1): #Blank space Row
        print(" ",end="")
    for j in range(startRow,endRow+1): #Number Row
        print(j,end="")
    print("")
    startRow -= 1
    endRow += 1
