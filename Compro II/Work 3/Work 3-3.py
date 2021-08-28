n = input("Enter number separate by space: ").split(" ")
print(n)

n.sort()
for i in range(0,len(n)-1):
    if(n[i] == n[i+1]): # Check current and next number
        print("Some numbers are repeated!!!")
        break
    elif(i == len(n)-2): # if last loop no have any same number will do this condition
        print("All numbers are different.")