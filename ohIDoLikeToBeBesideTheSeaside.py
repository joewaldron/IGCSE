# set up arrays for task 1, better style (2D)

volunteer_areas = ["No","Pier entrance gate","Gift shop","Painting and Decorating"]
members = []
# 2D array using the format [fname,lname,volunteer_code (0-3),join_date,paid]

# task 3 1D arrays
sponsor_names = []
sponsor_messages = []

# linear search function, not in question
def linearsearch(field, value, operator):
    outputlist = []
    for i in range(len(members)):
        add = False
        if operator == "=" and members[i][field] == value:
            add = True
        elif operator == ">" and members[i][field] > value:
            add = True
        elif operator == "<" and members[i][field] < value:
            add = True
        if add:
            outputlist.append(members[i][0] + " " + members[i][1])
    return outputlist

# menu system, not in question
choice = 0
while choice != 4:
    print("\n** Welcome to FOSP. **\n1 - join\n2 - search members\n3 - sponsor a plank\n4 - exit")
    choice = int(input("What do ya wanna do? "))
    if choice == 1:
        # need validators
        fname = input("Please enter your first name. ")
        sname = input("Please enter your surname. ")
        print("Many of our members volunteer. What can you help us with?\n0 - I'm not a helpful person")
        for v in range(1,len(volunteer_areas)):
            print(v,"-",volunteer_areas[v])
        volunteer_option = int(input("Please enter your choice. "))
        joindate = input("Please enter when you joined us. DD/MM/YY ")
        paid = input("Have you paid the $75 membership fee? Y/N ")
        new_member = [fname,sname,volunteer_option,joindate,paid]
        members.append(new_member)
    elif choice == 2:
        # task 2
        print("Search option. I don't understand SQL, sorry.\n0 - Volunteers")
        for v in range(1,len(volunteer_areas)):
            print(v,"-",volunteer_areas[v])
        print("4 - Expired Membership\n5 - Members who need to pay")
        search = int(input("Please enter your choice. "))
        results = []
        if search == 0:
            results = linearsearch(2,0,">")
        elif 0 < search < 4:
            results = linearsearch(2,search,"=")
        elif search == 4:
            results = linearsearch(3,"01/01/21","<")
        elif search == 5:
            results = linearsearch(4,"N","=")
        if len(results) > 0:
            print("Here are your search results:")
            for i in results:
                print(i)
        else:
            print("No members found.")
    elif choice == 3:
        # task 3
        confirm = False
        while not confirm:
            name = input("Please enter your name: ")
            msg = input("Please enter the message you want on your plank: ")
            print("You entered the following information.\nName: "+name+"\nMessage: "+msg+"\nIf you are happy to proceed, enter 'Y', or anything else to re-enter this information.")
            if input() == "Y":
                confirm = True
        print("Thanks, that'll be $200 for your plank please.")
        sponsor_names.append(name)
        sponsor_messages.append(msg)
