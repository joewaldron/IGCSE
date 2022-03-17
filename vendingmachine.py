#LO Understand concept of arrays (lists)
# Be able to use arrays (lists) to solve problems
# Use While and For loops to iterate through arrays (lists)

# The problem:
# Simulate a vending machine to sell snacks.
# The user asks for a snack, eg Coca Cola, and the machine tells the user
# if the machine sells it or not.

# Try to avoid doing this:
'''
item1 = "Coke"
item2 = "Stoney"
item3 = "Fanta"
item3 = "OJ"
# Instead, use an array to store multiple items of data.
items = ["Coke","Stoney","Sprite","Fanta","Water"] # an array of type String
# The index is the name given to the position of an item in an array.
# For example, items[0] is "Coke" and items[4] is "Water"
prices = [50,40,45,49,30] # an array of type integer
requested_item = input("What would you like to buy? ")
item_exists = False   # Boolean flag
for item in items:
    # Check to see if the requested_item exists in the machine.
    # one = CHANGE the value of the variable on the left with the result on the right
    # two == COMPARE the two values
    if item == requested_item:
        # If it exists, print out a message
        print("Yes we have that")
        item_index = items.index(item)
        print("Price:",prices[item_index])
        item_exists = True
        break   # stops the loop
        # If it does not, print out a message
if not item_exists:
    print("We don't have that")

# Linear search algorithm
# If the item exists, print its price.
# Tip: you will need to use a while loop to solve this problem.
position = 0
while position < 5:
    if items[position] == requested_item:
        print(prices[position])
    position = position + 1

'''
'''
Multiple line comment
1. # Extend the program by adding an array of quantities (stock level) for each item.
# The user asks for an item, you tell the user how much it costs.
# The user enters money - when the user enters enough money,
# If the item exists, AND there are more than zero in stock,
# 'Vend' the item (using print)
# Take one away from stock and print how many are left.
2. Put all of this in a while True: loop to repeat everything for the next customer.

3. Challenge 2:
Create a program to digitise your timetable to help students
Enter a day and period number and the program should tell you
which class and teacher you have.
Tips: You will need arrays for classes, teachers, and so on.
To start, make it work only for class names and one day (eg today) - this
will be very similar to the vending machine example without prices (1 array).
Then, add teachers - this is like the prices.
Then, think how to add different days (different solutions, could be harder).
'''
'''
# Understand how the for loop or while loop works with an array of data items.
alisa_shopping_list = ["loaves of bread","bottles of water","packets of milk","potatoes","Cadbury choc and biscuits","oranges","passion fruits","yoghurts","bananas"]
#                       ^pos 0  ^pos 1  ^pos 2  ^pos 3       ^pos 4
alisa_quantities =    [   6   ,  2    ,  10  ,  50      , 3,34,132,345,5]
alisa_prices = [42,30,43,5,200,20,50,10,1]
#print(alisa_shopping_list[4])
alisa_shopping_list[1] = "Cokes"
# Write the instruction using print to print out a sentence describing how many
# potatoes we need: "Alisa needs 50 potatoes"
print("Alisa needs",alisa_quantities[0],alisa_shopping_list[0])

print("The next output uses our while loop")
total = 0
position = 0  # an integer that we will use to reference the position in the list.
while position < len(alisa_shopping_list):  # len will tell us how many things are in the list
    print("Alisa needs",alisa_quantities[position],alisa_shopping_list[position])
    total = total + alisa_prices[position] * alisa_quantities[position]
    position = position + 1
# Index out of range error - what is it?
print("The total cost will be",total,"Ksh.")
'''
# Your task: Create a program that stores student names and test scores/100 in the class
# Output the average score (easy) and
# the name of the student with their highest score (a little bit harder)

