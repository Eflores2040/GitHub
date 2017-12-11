## Edgar Flores

## October 18, 2017

# Character Replacer
def replacer(phrase,replacewh,replacewi):
    result = ""
    for ch in phrase:
        if ch == replacewh:
            result += replacewi
        else:
            result += ch
    return result

phrase = input("What is the phrase?")
replacewh = input("What character do you want to replace?")
replacewi = input("What do you want to replace that character with?")

nphrase = replacer(phrase,replacewh,replacewi)

print("The new phrase is %s" % nphrase)

    
