# CodeWars
# 17/6/2023

# Sum of 2 smallest integers in an array
def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.pop(numbers.index(min(numbers)))
    return min1 + (min(numbers))

# Return all positive values in array
def positive_sum(arr):
    output = 0
    for value in arr:
        if value > 0:
            output += value
    return output

# I dont even know what this does
def comp(a, b):
    return sorted(a) == sorted([num ** 2 for num in b]) if a and b else False