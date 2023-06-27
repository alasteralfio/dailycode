# CodeWars
# 26/6/2023

# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
def bouncing_ball(h, bounce, window):
    count = 0
    if h <= window or bounce <= 0 or bounce >= 1:
        return -1
    while h > window:
        h = h * bounce
        if h > window:
            count += 1
    return count + 1