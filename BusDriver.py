# 1D basis: CIE preferred

busA = []
busB = []
busC = []
busD = []
busE = []
busF = []

# 2D basis: easier!

busData = []    # needs init

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
routes = ["A", "B", "C", "D", "E", "F"]

# initialise busData
for bus in range(len(routes)):
    busData.append([])

for week in range(1, 5):
    for day in weekdays:
        for bus in range(len(routes)):
            nextbus = 999
            while nextbus < -240 or nextbus > 240:  # shouldn't be earlier or later than this
                nextbus = input("Enter data for Bus " + routes[bus] + " on " + day + str(week) + ": ")
                try:
                    nextbus = int(nextbus)
                except ValueError:
                    print("Please enter a number.")
                    nextbus = 999   # error condition - type check
            busData[bus].append(nextbus)
            exec("bus"+routes[bus] + ".append(nextbus)")    # not good practice but I am too lazy to build this as a function

# Task 2: Stats

maxlate = 0
maxlatepos = 0
print("         Late Arrivals    Avg Delay    Avg Delay on Late Days")
for eachroute in range(len(busData)):
    latecount = 0
    totaldelay = 0
    for eachday in busData[eachroute]:
        if eachday < 0:
            latecount += 1
            totaldelay += eachday
    totaldelay = abs(totaldelay)
    if latecount > maxlate:
        maxlate = latecount
        maxlatepos = eachroute
    averagedelay = totaldelay / len(busData[eachroute])
    if latecount > 0:
        averagedelaylatedays = str(round(totaldelay / latecount, 2))
    else:
        averagedelaylatedays = "N/A"
    print("Bus " + routes[eachroute] + ":" + " "*10 + str(latecount) + " "*(13-len(str(latecount))) + str(round(averagedelay,2)) + " "*15 + averagedelaylatedays)
print("\nThe bus route with the most delays was Bus " + routes[maxlatepos] + " with " + str(maxlate) + " late arrivals.")

# Task 3
chosenDay = "Dddn"
while chosenDay[0:3] not in weekdays:
    chosenDay = input("Please enter the day to look up, in the format Dddn: ")
    if len(chosenDay) != 4:
        chosenDay = "Dddn"
    if not chosenDay[3].isnumeric():
        chosenDay = "Dddn"

day = weekdays.index(chosenDay[0:3])
weekmultiplier = int(chosenDay[3])
position = (weekmultiplier-1 * len(weekdays)) + day
count = 0
outstr = ""
for bus in range(len(busData)):
    if busData[bus][position] < 0:
        count += 1
        outstr += "Bus " + routes[bus] + " was " + str(abs(busData[bus][position])) + " minutes late on " + chosenDay + "\n"
print("There were " + str(count) + " delayed buses.")
print(outstr)
