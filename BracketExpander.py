import re

def multiply(a,b):
    if not re.search('[^0-9^\-]', a):
        a = int(a)
        if not re.search('[^0-9^\-]', b):
            b = int(b)
            finstring = str(a*b)
        else:
            p = re.search('[^0-9]',b)
            if p:
                c = int(b[0:p.start()])
                b = b[p.start():]

                finstring = str(a*c)+b
            else:
                finstring = str(a)+b
    elif not re.search('[^0-9^\-]',b):
            b = int(b)
            p = re.search('[0-9]',a)
            if p:
                c = int(a[p.start():p.end()])
                a = a[p.end():]

                finstring = str(b*c)+a
            else:
                finstring = str(b)+a

    else:
        p = re.search('[0-9]',b)
        if p:
            c = int(b[p.start():p.end()])
            b = b[p.end():]

            finstring = str(c)+min(b,a)+max(b,a)
        else:
            p = re.search('[0-9]',a)
            if p:
                c = int(a[p.start():p.end()])
                a = a[p.end():]

                finstring = min(b,a)+max(b,a)
            else:
                finstring = str(b)+a

    if "-" not in finstring: return "+"+finstring
    else: return finstring

#startingproblem = input("Please enter your maths problem. Use ^ for indices.\n")
#example input accepted = (x+3)(y-3)
startingproblem = "(x+3)(2y-3)"
finishedproblem = ""
brackets = []
for character in range(len(startingproblem)):
    if startingproblem[character] == "(":
        bpos = character
    if startingproblem[character] == ")":
        bracket = startingproblem[bpos+1:character]
        if not "-" in bracket:
            brackets.append(re.split("[\+]",bracket))
        else:
            pos = bracket.index("-")
            brackets.append([bracket[0:pos],bracket[pos:]])
print(brackets)
#FOIL method implementation
for x in range(2):
    for y in range(2):
        finishedproblem += multiply(brackets[0][x],brackets[1][y])
if finishedproblem[0] == "+":
    finishedproblem = finishedproblem[1:]
print(finishedproblem)
