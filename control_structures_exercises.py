#Conditional Basics

#prompt the user for a day of the week, print out whether the day 
# is Monday or not

day_of_the_week = input("What day of the week is it?")
if day_of_the_week == "Monday":
    print("Today is Monday.")
else:
    print("Today is not Monday.")


#prompt the user for a day of the week, print out whether the day 
#is a weekday or a weekend

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
week_end = ['Saturday', 'Sunday']

what_day = input('Do I have to work today? Is today a weekday?')
if what_day in week_days:
    print('Yes, you do. Yes, it is.')
elif what_day in week_end:
    print('No, you don\'t. No, it isn\'t.')
else:
    None

#create variables and make up values for:

#the number of hours worked in one week

work_hours = float(input("Hours worked:"))

#the hourly rate

hourly_rate = 48

#how much the week's paycheck will be

paycheck = work_hours * hourly_rate
print(f"Your paycheck this week is: ${paycheck}")


#write the python code that calculates the weekly paycheck. You 
# get paid time and a half if you work more than 40 hours

hours_overtime = float(input("Overtime worked:"))
time_and_a_half = hourly_rate * 1.5
if hours_overtime >= 1:
    paycheck = (40 * hourly_rate) + (hours_overtime * time_and_a_half)

print(f"Your paycheck this week is: {paycheck}")

#While

#Create an integer variable i with a value of 5.

i = 5

#Create a while loop that runs so long as i is less than or equal 
#to 15

while i <= 15:
    print(i)
    i += 1



#Create a while loop that will count by 2's starting with 0 and 
# ending at 100. Follow each number with a new line.

h = 0
while h % 2 == 0 and h <= 100:
    print(h)
    h += 2

#Alter your loop to count backwards by 5's from 100 to -10.

h = 100
while h >= -10:
    print(h)
    h -= 5

#Create a while loop that starts at 2, and displays the number 
# squared on each line while the number is less than 1,000,000.

g = 2
while g < 1000000:
    print(g)
    g **= 2
  
#Write a loop that uses print to create the output shown 
# (in last codeup while exercise)

f = 100
while f >= 5:
    print(f)
    f -= 5

# For Loops

#Write some code that prompts the user for a number, then shows a 
# multiplication table up through 10 for that number.

x = int(input('Enter a number:'))
for n in range(1, 11):
    print(f'{x} x {n} = {x * n}')
    n += 1
    
# Create a for loop that uses print to create the output shown
# in (codeup for exercises ii)

for y in range(1, 10):
    print (f'{y}' * y)
    y += 1

# Prompt the user for an odd number between 1 and 50. Use a loop 
# and a break statement to continue prompting the user if they 
# enter invalid input. (Hint: use the isdigit method on strings 
# to determine this). Use a loop and the continue statement to 
# output all the odd numbers between 1 and 50, except for the 
# number the user entered.

while True:
    z = int(input('Enter an odd number between 1 and 50:'))
    if z in range(1, 50) and z % 2 != 0:
        print(f'Number to skip is: {z}')
    else:
        print ('Invalid input. Try again.')
    
    for n in range(1,50):
        if n % 2 != 0:
            print(f'Here is an odd number: {n}')
        elif n == z:
            print(f'Yikes! Skipping number: {z}')




    