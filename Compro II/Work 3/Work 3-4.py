n = input("Enter 5 numbers seperated by space: ")
n = list(map(int,n.split(" ")))
print("Original:",n)

print("Step 1: Add 8 and 4 to the end of the list")
n.append(8)
n.append(4)
print("    ",n)

print("Step 2: insert 2 after 3 and 6 after 5")
n.insert(1,2)
n.insert(4,6)
print("    ",n)

print("Step 3: remove 1 and 8")
n.remove(1)
n.remove(8)
print("",n)