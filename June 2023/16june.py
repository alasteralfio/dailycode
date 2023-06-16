# CodeWars
# 16/6/2023

# Check for x in array a.
def check(seq, elem):
    for char in seq:
        if char == elem:
            return True
    return False

# Abbreviate to initials
def abbrev_name(name):
    name = (name.split())
    output = ''
    for ini in name:
        output += ini[0].upper() + '.'
    return output[:-1]

# Reverse string
def solution(string):
    return string[::-1]