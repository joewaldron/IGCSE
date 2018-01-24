weekly_milk_yields = []
herdsize = 0
setup = False
milkentries = 0
maxmilkperweek = 14

def milk():
    global weekly_milk_yields
    cow = int(validateinput(1,999,"the cow identity code"))
    yieldamount = validateinput(0,50,"the amount of milk in litres")
    weekly_milk_yields.append([cow,yieldamount])

def validateinput(start,end,descriptor):
    number = -1
    while start > number or end < number:
        number = float(input("Please enter "+descriptor+ " between " +str(start) + " and " + str(end) + ": "))
    return number

def printstats():
    total = 0
    global herdsize
    totalspercow = {}
    maxcowID = 0
    maxcowyield = 0
    cow_checked = []
    cowundermilking = []
    for cow in weekly_milk_yields:
        total += cow[1]
        #totalspercow[cow[0]] += cow[1]  #non-CIE style
        #CIE style
        if not cow[0] in cow_checked:
            thiscowtotal = 0
            undermilkcount = 0
            dailyflag = 0
            dailytotal = 0
            for thiscow in weekly_milk_yields:
                if thiscow[0] == cow[0]:
                    thiscowtotal += thiscow[1]
                    if dailyflag == 0:
                        dailytotal = 0
                        dailytotal += thiscow[1]
                        dailyflag = 1
                    elif dailyflag == 1:
                        dailytotal += thiscow[1]
                        dailyflag = 0
                        if dailytotal < 12 :
                            undermilkcount += 1
            if thiscowtotal > maxcowyield:
                maxcowyield = thiscowtotal
                maxcowID = cow[0]
            if undermilkcount >= 4:
                cowundermilking.append(cow[0])
            cow_checked.append(cow[0])

    print("The total milk this week is " + str(round(total)) + " litres.")
    print("The average per cow is " + str(round(total/herdsize)) + " litres.")
    print("The cow with the greatest yield was " + str(maxcowID) + " which produced " + str(maxcowyield) + " litres of milk this week.")
    if len(cowundermilking) > 0:
        print("The following cows produced less than 12 litres for four days or more in the week:")
        for eachcow in cowundermilking:
            print("Cow ID: " + str(eachcow))

def menu():
    global herdsize
    global setup
    global milkentries
    print("Welcome to the milk management system.")
    option = int(input("Enter 1 to enter milking data, 2 for statistics or 3 to exit.\n"))
    if option == 3:
        return
    elif option == 2:
        printstats()
    elif option == 1:
        if not setup:
            print("The herd size has not been configured.")
            herdsize = int(validateinput(0,999,"the number of cows in the herd"))
            setup = True
        if milkentries < maxmilkperweek:
            for count in range(herdsize):
                milk()
                print(str(herdsize-count-1) + " cows remaining to enter")
            milkentries += 1
        else:
            print("Sorry, you have already milked the cows 14 times this week.")
    menu()

menu()
