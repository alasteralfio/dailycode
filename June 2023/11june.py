# CodeWars
# 11/6/2023

# Your task is to write a function which returns the time since midnight in milliseconds.
def past(h, m, s):
    ms = 0
    ms += h * 3600000
    ms += m * 60000
    ms += s * 1000
    return ms

# Write a function which calculates the average of the numbers in a given list.
def find_average(numbers):
    if numbers:
        ave = sum(numbers) / len(numbers)
    else:
        ave = 0
    return ave

# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
def solution(s):
    if len(s) % 2 == 0:
        pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    else:
        pairs = [s[i:i+2] for i in range(0, len(s)-1, 2)]
        pairs.append(s[-1] + '_')
    return pairs