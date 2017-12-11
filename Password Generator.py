# Edgar Flores

#Password Generator

## 24 October, 2017
import random

'''
functions
'''
def second_part (m):  ##replacing letters
    new_word = ""
    for ch in m:
        if ch == "i":
            new_word += "1"
        elif ch == "I":
            new_word += "1"
        elif ch == "s":
            new_word += "$"
        elif ch == "S":
            new_word += "$"
        elif ch == "o":
            new_word += "0"
        elif ch == "O":
            new_word += "0"
        else:
            new_word += ch
    return new_word
            
            
        
   # main  
file = input("Enter the name of the file that contains the word list:")
filvar= open(file,"r")
how_many = int(input("How many passwords do you want to create?"))
print("Here are the passwords:")
words = []
for line in filvar: #opening file
    line = line.strip()
    words.append(line)
for i in range (how_many):
    first = random.choice(words).strip() #first part of password
    second = second_part(random.choice(words)).upper().strip() #second part of password
    third = random.choice(words).strip() #third part of password
    num = str(random.randint(1000,9999)).strip() ##random number generater
    password = (first+second+third+num).strip() #final password
    print("%s" % password)
  
        
       
filvar.close() #closing the file
