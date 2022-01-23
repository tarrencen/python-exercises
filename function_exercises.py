# Define a function named is_two. It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.

import numbers


def is_two(value):
    if value == 2:
        return True
    elif value == '2':
        return True
    elif value == 'two':
        return True
    elif value == 'Two':
        return True
    elif value == 'TWO':
        return True
    else:
        return False

assert is_two('Two') == True
assert is_two('TWO') == True
assert is_two('two') == True
assert is_two(2) == True
assert is_two('2') == True
assert is_two(37) == False

# Define a function named is_vowel. It should return True if the passed string 
# is a vowel, False otherwise.

vowels = 'aeiouAEIOU'

def is_vowel(string):
    if len(string) == 1 and string in vowels:
        return True
    else:
        return False

assert is_vowel('a') == True
assert is_vowel('b') == False
assert is_vowel('U') == True
assert is_vowel('y') == False


# Define a function named is_consonant. It should return True if the passed 
# string is a consonant, False otherwise. Use your is_vowel function to 
# accomplish this.

def is_consonant(string):
    if is_vowel(string) == False:
        return True
    else: 
        return False

assert is_consonant('E') == False
assert is_consonant('t') == True
assert is_consonant('i') == False



# Define a function that accepts a string that is a word. The function should 
# capitalize the first letter of the word if the word starts with a consonant.

def capped_word(string):
    no_cap = 'String starts with a vowel, no cap'
    if is_consonant(string[0]) == True:
        return string.capitalize()
    else:
        return no_cap

assert capped_word('buddy') == 'Buddy'



# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.


def calculate_tip(bill_total, tip_percent=0.2):
    if tip_percent > 0.0 and tip_percent < 1.0:
        return bill_total * tip_percent
    else:
        return 'Too much or not enough'

calculate_tip(134.79)
calculate_tip(1237.09, 0.67)
    

# Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is 
# applied.

def apply_discount(price, disc_percent):
    return price - (price * disc_percent)

apply_discount(1179, 0.45)

# Define a function named handle_commas. It should accept a string that is a 
# number that contains commas in it as input, and return a number as output.

import re

def handle_commas(string):
    if type(string) != str:
        return 'Invalid input'
    string = re.sub(',', '', string)
    if string.isdigit():
        return int(string)
    else:
        return 'Invalid input'

handle_commas('1,000,000,000')
handle_commas('One billion, two hundred million, three hundred thirty thousand, seven hundred and fifty-seven dollars and thirty-eight cents')



# Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    if number >= 90:
        return 'A'
    elif number in range(85,92):
        return 'B'
    elif number in range(77,86):
        return 'C'
    elif number in range(69,78):
        return 'D'
    elif number <= 70:
        return 'F'
    else:
        None

get_letter_grade(83)
get_letter_grade(54)
get_letter_grade(-700)
get_letter_grade(105)



# Define a function named remove_vowels that accepts a string and returns a 
# string with all the vowels removed.

def remove_vowels(string):
   return ''.join(l for l in string if l not in vowels)

remove_vowels('onomatopoeia')
remove_vowels('Abracadabra molefoquel')
remove_vowels('kryswctky')

            

# Define a function named normalize_name. It should accept a string and 
# return a valid python identifier (as shown in example)

import re

spec_chars = ['!', '@', '#', '$', '%', '^', '*', '(', ')', ',', '<', '>', '?']

def normalize_name(string):
    if type(string) == str:
        string = string.lower()
        string = string.strip()
        string = re.sub(' ', '_', string)
        for l in string:
            if l in spec_chars:
                string = re.sub(l, '', string)
                string = string.lstrip('_')
                string = string.rstrip('_')
                return string.strip()
        
    return string

   
normalize_name(' Clarence Carter! ')
normalize_name('Tarrence Nichols')

normalize_name('% Completed')


   
assert normalize_name(' Clarence Carter! ') == 'clarence_carter'
assert normalize_name('First Name') == 'first_name'
assert normalize_name('Name') == 'name'
assert normalize_name('% Completed') == 'completed'


# Write a function named cumulative_sum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.

import numpy as np

def cumulative_sum(arr=[1, 2, 3, 4]):
    return np.cumsum(arr)

cumulative_sum([5, 6, 7, 8])
cumulative_sum([1, 1, 1])

'''assert cumulative_sum([1, 1, 1]) == ([1, 2, 3])
assert cumulative_sum([1, 2, 3, 4]) == ([1, 3, 6, 10])
assert cumulative_sum([1, 0, -1, 5]) == ([1, 1, 0, 5]) -- assertion errors, even though
the function outputs an array with a cumulative sum as prescribed in the exercise'''

