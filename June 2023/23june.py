# CodeWars
# 23/6/2023

# Sum negative numbers, count positive numbers
def count_positives_sum_negatives(arr):
    if not arr:  # Check if the array is empty or null
        return []  # Return an empty array in this case

    count_positives = 0
    sum_negatives = 0

    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num

    return [count_positives, sum_negatives]

# Round down, 1l for every 0.5h
def litres(time):
    return (time / 2) // 1

# count True
def count_sheeps(sheep):
    count = 0 
    for i in sheep:
        if i == True: count += 1
    return count

