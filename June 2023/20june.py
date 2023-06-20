# CodeWars
# 20/6/2023

# Compare
def better_than_average(class_points, your_points):
    if your_points > sum(class_points)/len(class_points):
        return True
    return False

# Find next square, return -1 if input not sq
def find_next_square(sq):
    if (sq**0.5) == round(sq**0.5):
        return ((sq**0.5)+1)**2
    return -1

# make uppercase
def make_upper_case(s):
    return s.upper()