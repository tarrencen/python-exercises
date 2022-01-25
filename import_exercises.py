import function_exercises as fe
fe.is_vowel('e')

#How many different ways can you combine the letters from "abc" with the numbers 1, 2, 
# and 3?
from itertools import permutations, combinations

abc123_combos = list(combinations (, 2))

    
#How many different combinations are there of 2 letters from "abcd"?

abcd_combolist = list(combinations('abcd', 2))
len(abcd_combolist)

#How many different permutations are there of 2 letters from "abcd"?

abcd_permlist = list(permutations('abcd', 2))
len(abcd_permlist)

import json

dict_list = list(json.load(open('profiles.json')))


# Your code should produce a list of dictionaries. Using this data, write some code that calculates 
# and outputs the following information:

#Total number of users

profile_count = len(dict_list)
print(profile_count)

# 19 total users

#Number of active users

for i in dict_list:
    i.keys()

j = [i.get('isActive') == True for i in dict_list]

print(j)
for k in j:
    if k == false:









    


#Number of inactive users
#Grand total of balances for all users
#Average balance per user
#User with the lowest balance
#User with the highest balance
#Most common favorite fruit
#Least most common favorite fruit
#Total number of unread messages for all users


