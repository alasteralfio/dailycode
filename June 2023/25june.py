# CodeWars
# 25/6/2023

# each dragon takes 2 bullets
def hero(bullets, dragons):
    return (bullets / 2) >= dragons

# move 0 to end of array
def move_zeros(lst):
    zeros = []
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            zeros.append(lst.pop(i))
        else:
            i += 1
    lst.extend(zeros)
    return lst

# Sum digits in a number
def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))