# Course: IT-140-H7801
# Lab: 2.13 Lab: Count Characters
# Date: 2023/09/10
# Name: Rickey Partridge
# Description: Program that counts number of times a character appears in a string.

###########################################################

#    Title: Python.org
#    Author: Python Software Foundation
#    Date: Jan 3, 2018
#    Code version: 3.11.5
#    Availability: https://docs.python.org/3/library/stdtypes.html#str.count
#

###########################################################

# User input
input_string = input()

# String split
input_char = input_string[0]

compare_string = input_string[1:]

# Output character count
print(compare_string.count(input_char))
