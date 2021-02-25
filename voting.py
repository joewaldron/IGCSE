# Pre Release Task May 2021

# Task 1: Setting up the candidates and data structures
# Using 1D arrays for each category

# Not needed for task: Storing elected representatives
school_representatives = []


for tutor_group in range(30): # repeat for all tutor groups in school
    invalid = True
    # Validation check: Format and length check
    while invalid:
        name = input("Please enter the name of the tutor group: ")
        if len(name) == 2 and (name[0] == '7' or name[0] == '8' or name[0] == '9') and name[1].isalpha():
            invalid = False
        elif len(name) == 3 and (name[0:2] == '10' or name[0:2] == '11') and name[2].isalpha():
            invalid = False
        # not needed for task
        for check in school_representatives:
            if check[0] == name:
                invalid = True
                print("Voting for this form has already concluded.")
    num_students = int(input("Please enter the number of students in " + name + ": "))
    # Range check
    while num_students < 28 or num_students > 35:
        num_students = int(input("Please enter the correct number of students in " + name + ": "))

    num_candidates = int(input("How many candidates are standing for the election? "))
    # Range check
    while num_candidates < 1 or num_candidates > 4:
        num_candidates = int(input("How many candidates are standing for the election? Maximum 4: "))

    candidate_names = ["Abstain"]    # set up new array for this class only
    student_votes = [0]      # set up array for student votes
    for candidate in range(num_candidates):
        candidate_names.append(input("Please enter the name of candidate " + str(candidate+1) + ": "))
        student_votes.append(0)
    # Voting begins here. The while loop is for task 3.
    single_winner = False
    while not single_winner:
        total_votes = 0
        student_ids = []    # set up array to record those students who have already voted, for task 2
        while total_votes < num_students:
            # Task 2 extends Task 1 here
            voter_num = input("Welcome. Please enter your unique voter number: ")
            # Should really use a linear search to confirm they haven't voted... but I shall be lazy.
            # You can expect to explain the linear search that should be here for one of the questions though!
            if voter_num in student_ids:
                print("Hey! You've voted already. ")
                continue    # this will restart the loop by returning to the while condition.
                # You could alternatively use a Boolean flag here eg allowed_to_vote = False.
            else:
                student_ids.append(voter_num)
                total_votes += 1

            print("Welcome. Please choose from the following candidates:")
            for candidate in range(len(candidate_names)):
                print(str(candidate) + ": " + candidate_names[candidate])
            choice = input("Please enter the number of the choice you wish to make, or 0 to abstain: ")
            # validate choice
            while choice.isalpha(): # make sure it was a number entered! try...except not in igcse.
                choice = input("You just need to enter the NUMBER of the candidate here, or 0 to abstain: ")
            choice = int(choice)
            while choice < 0 or choice > num_candidates:
                choice = int(input("That's not a valid candidate number, please try again: "))
            # This will not catch a string entry on the second validator.
            student_votes[choice] += 1
            print("Thanks for voting.")
        print("Voting has finished.")
        print("Tutor group: " + name)
        highest_votes = 0
        # For task 3, I have added the percentage calculation here.
        total_abstentions = student_votes[0]
        print("There were a total of " + str(total_votes) + " votes cast and " + str(total_abstentions) + " abstentions.")
        for result in range(1, len(candidate_names)):
            print("Candidate " + candidate_names[result] + " received " + str(student_votes[result]) + " votes.")
            print("That's " + str(student_votes[result]/(total_votes-total_abstentions)*100) + "% of votes cast.")
            if student_votes[result] > highest_votes:   # This will not count abstentions
                highest_votes = student_votes[result]

        winners = []
        for winner in range(1, len(candidate_names)):   # Not counting abstentions
            if student_votes[winner] == highest_votes:
                winners.append(candidate_names[winner])
        # Check to see if abstentions 'won'. Do we need to do this? NO.
        #if winners[0] == "Abstain":
        #    print("Unfortunately, there is no winner this time. Voting will begin again.")
        if len(winners) == 1:
            print("The winner is... " + winners[0])
            single_winner = True  # stops the election repeating
        else:
            print("It's a tie! The following candidates have tied in first place:")
            for winner in winners:
                print(winner)
            # Task 3: We need to restart the voting. Reset the votes...
            candidate_names = winners
            if "Abstain" not in candidate_names:
                candidate_names.insert(0,"Abstain")
            student_votes = []
            for candidate in candidate_names:
                student_votes.append(0)
    print("Ready to begin the election process for the next class.")

    # not needed for task
    school_representatives.append([name,winners[0]])
print("Elections for all tutor groups have now finished. The class representatives are as follows:")
for rep in school_representatives:
    print(rep[0] + ": " + rep[1])
