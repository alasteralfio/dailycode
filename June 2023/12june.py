# CodeWars
# 12/6/2023

# Given an integral number, determine if it's a square number:
def is_square(n):    
    if n >= 0 and (n**(1/2)) % 1 == 0: return True
    else: return False

# Your task is to write a function that takes a string and return a new string with all vowels removed.
def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in string_:
        if char not in vowels:
            result += char  # Append the non-vowel character to the result string
    return result

# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
def array_diff(a, b):
    result = []
    for char in a:
        if char not in b:
            result.append(char)
    return result