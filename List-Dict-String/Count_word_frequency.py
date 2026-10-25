paragraph = "Python is easy. Python is fun!"

frequency = {}
word = ""

for character in paragraph + "":
    if ("a" <= character <="z") or ("A" <= character<="Z"):
        word =  word+character
    else:
        if word !="":
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word] = 1
            word = ""

print(frequency)
