instring = input("Pls, ur word: ").upper()
characters = []
count = []      #using 1D arrays in parallel, CIE style
index = 0
while index < len(instring):
    if instring[index] in characters:
        count[characters.index(instring[index])] += 1
    else:
        characters.append(instring[index])
        count.append(1)
    index += 1
for eachchar in range(len(characters)):
    print(characters[eachchar]+": "+str(count[eachchar]))
