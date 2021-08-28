word = input("Enter a sentence: ")
print("\"%s\""%word)

letter = 0
number = 0

for i in word:
    if( i.isalpha() == True ): # isalpha is check letter
        letter += 1
    elif( i.isdigit() == True ): # isdigit ischeck number
        number += 1

print("    contains %d letter(s) and %d digit(s)"%(letter,number))