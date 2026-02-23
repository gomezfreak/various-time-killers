# Course: IT-140-H7801
# Lab: 2.14.1 Lab: Warm up: Creating passwords
# Date: 2023/09/10
# Name: Rickey Partridge
# Description: Program that creates two simple passwords from three user inputs.

# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
# Add two entries to capture favorite flower and favorite number
favorite_color = input()
favorite_flower = input()
favorite_number = input()

# Print all 3 entries on one line
print('You entered:', favorite_color, favorite_flower, favorite_number)

# FIXME (2): Output two password options
password1 = favorite_color + '_' + favorite_flower
password2 = favorite_number + favorite_color + favorite_number

print('\nFirst password:', password1)
print('Second password:', password2)

# FIXME (3): Output the length of the two password options
# Output length of passwords using len
print('\nNumber of characters in', password1 + ':', len(password1))
print('Number of characters in', password2 + ':', len(password2))
