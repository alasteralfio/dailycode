# CodeWars
# 9/6/2023

# Build a function that returns an array of integers from n to 1 where n>0.
def reverse_seq(n):
    num = []
    for i in range(n, 0, -1):
        num.append(i)
    return num

# You are given a string representing a number in binary. Your task is to delete all the unset bits in this string and return the corresponding number (after keeping only the '1's).
def eliminate_unset_bits(number):
    digits = list(str(number))
    digits = [digit for digit in digits if digit != '0']
    if not digits:
        return 0
    binary = ''.join(digits)
    decimal = int(binary, 2)
    return decimal

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
def is_isogram(string):
    
    # Sets string to lowercase for comparisons
    string = string.lower()
    
    # splices the string into individual letters
    letters = string[::1]
    if len(letters) == 0:
        return True
    for letter in letters:
        
        # Keeping count of each letter
        if letters.count(letter) > 1:
            return False
    return True