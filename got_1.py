import sys
import string
o_string = raw_input()
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
# First thought - Every letter has to occur even number of times. Let's build a dict of letters, and later check it.
alph_dict = dict.fromkeys(string.ascii_lowercase, 0)

for letter in o_string:
    alph_dict[letter] += 1;
odd_counter = 0
for key in alph_dict:
    if alph_dict[key] % 2 != 0:
        odd_counter += 1
        
if len(o_string) %2 == 1 and odd_counter == 1:
    pass
elif odd_counter > 0:
    found = False

if not found:
    print("NO")
else:
    print("YES")
