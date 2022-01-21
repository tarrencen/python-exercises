#You have rented some movies for your kids: The little mermaid 
# (for 3 days), Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like 
# it). If price for a movie per day is 3 dollars, how much will 
# you have to pay?

movie_rental = 3
little_mermaid = 3
brother_bear = 5
hercules = 1
print((little_mermaid * movie_rental) + (brother_bear * movie_rental) + (hercules * movie_rental))

#Suppose you're working as a contractor for 3 companies: Google, 
# Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 
# 10 hours for Facebook, 6 hours for Google and 4 hours for 
# Amazon.

gugul = 400
tall_chik = 380
zuckold = 350

this_weeks_work = (10 * zuckold) + (6 * gugul) + (4 * tall_chik)
print(this_weeks_work)

#A student can be enrolled to a class only if the class is not full and the 
#class schedule does not conflict with her current schedule.


class_full = False
schedule_conflict = False

student_enrollment = not class_full and not schedule_conflict

# A product offer can be applied only if people buy more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.


more_than_two_items = True
offer_expired = False
premium_member = True

product_offer = not offer_expired and (more_than_two_items or premium_member)

#Continue working in your data_types_and_variables.py file. Use the 
# following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

#Create a variable that holds a boolean value for each of the following 
# conditions:

len(password) > 5
len(username) < 20
password != username
username = username.strip()
password = password.strip()


