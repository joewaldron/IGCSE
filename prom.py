# Task 1

max_students = 50
venue_cost = 800
dj_cost = 150
meal_baserate = 12

number_attendees = int(input("Pls enter how many students are coming. "))
while not 0 < number_attendees <= max_students:
    number_attendees = int(input("Pls enter how many students are coming. Minimum 1, maximum " + str(max_students) + ": "))
fixed_costs = dj_cost + venue_cost
fixed_costs_per_attendee = fixed_costs / number_attendees
total_meal_cost = meal_baserate * number_attendees
discount = number_attendees // 9     # every 9th meal free
meal_per_person = (total_meal_cost - discount) / number_attendees
cost_per_person = meal_per_person + fixed_costs_per_attendee
print("The minimum charge per student should be $" + str(round(cost_per_person, 2)))
rec_cost_per_person = cost_per_person * 1.04
print("The recommended charge, based on 4% expected non-attendance, is $" +str(round(rec_cost_per_person, 0)))

# Task 2

student_names = []
paid_status = []
valid_students_entered = 0
while valid_students_entered < number_attendees:
    next_name = input("Please enter the name of attendee number " + str(valid_students_entered+1) + " ")
    if next_name in student_names:
        print("This attendee has already been entered.")
        continue
    paid = input("Have they paid? ")
    if 'Y' in paid.upper():
        paid = True
    elif 'N' in paid.upper():
        paid = False
    else:
        print("Invalid input, try again.")
        continue
    student_names.append(next_name)
    paid_status.append(paid)
    valid_students_entered += 1

# List of paid / unpaid students
pos = 0
paidout = ""
paid_count = unpaid_count = 0
unpaidout = ""
for pos in range(number_attendees):
    if paid_status[pos]:
        paidout += student_names[pos] + "\n"
        paid_count += 1
    else:
        unpaidout += student_names[pos] + "\n"
        unpaid_count += 1

print("The following " + str(paid_count) + " students have paid:\n" + paidout)
print("The following " + str(unpaid_count) + " students have NOT paid:\n" + unpaidout)
# Task 3
total_cost = round(number_attendees*meal_per_person+fixed_costs,2)
total_collected = round(paid_count*round(rec_cost_per_person,0),2)   # uses recommended costs
print("Total cost of event: $" + str(total_cost))
print("Total money collected: $" + str(total_collected))
if total_collected < total_cost:
    print("A loss of $" + str(round(total_cost-total_collected,2)) + " was made.")
elif total_collected > total_cost:
    print("A profit of $" + str(round(total_collected-total_cost,2)) + " was made.")
else:
    print("The event broke even.")
