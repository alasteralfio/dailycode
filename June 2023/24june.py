# CodeWars
# 24/6/2023

# min and max
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

# Find unique number
def find_uniq(arr):
    for i in arr:
        if arr.count(i) == 1:
            unique_num = i
            break
    return unique_num