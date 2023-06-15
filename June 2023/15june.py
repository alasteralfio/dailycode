# CodeWars
# 15/6/2023

# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
def first_non_repeating_letter(s):
    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return ""

# sum of array
def sum_array(a):
    total = sum(a)
    return total

# Remove first and last char
def remove_char(s):
    char = list(s)
    char.pop(0)
    char.pop(-1)
    return ''.join(char)