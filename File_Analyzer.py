### Edgar Flores

## 12 October 2017

## File Analyzer

file = input("Enter the name of the file you would like to analyze:")
filvar = open(file,"r") 
word = 0
sent = 0 # sentences
punk = 0 # punctuation
con = 0 # consonants
vowel= 0
lines = 0
print("This is the file I am analyzing:")
for line in filvar:
    line = line.strip()
    lines += 1
    print(line)
    for i in line:
        if i in ".?!":
            sent += 1
        if i in "aeiouAEIOU":
            vowel += 1
        if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            con += 1
        if i in " ":
            word += 1
        if i in ",.':;()!?":
            punk += 1
filvar.close()
print("Results:")
print("Lines: %d" % lines)
print("Words: %d" % word)
print("Sentences: %d" % sent)
print("Punctuation: %d" % punk)
print("Consonants: %d" % con)
print("Vowels: %d" % vowel)

    
    
        
