while(True):
    n_word = int(input("How many word? (3-5) : "))
    if(n_word >= 3 and n_word <= 5):
        break
    else: print("Invalid Number!!!")

dict = {}
for i in range(1,n_word+1):
    temp = input("Word %d: "%i)
    dict.update({temp:len(temp)})

print("Data in the dictionary:",dict)