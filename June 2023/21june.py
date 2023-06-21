# CodeWars
# 21/6/2023

# Likes counter
def likes(names):
    output = ''
    if len(names) == 0:
        output = 'no one likes this'
    elif len(names) == 1:
        output = f'{names[0]} likes this'
    elif len(names) == 2:
        output = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        output = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        output = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    return output

# Join array into string
def smash(words):
    return ' '.join(words)

# square every digit of a number and concatenate them.
def square_digits(num):
    num = str(num)
    output = []
    for digit in num:
        digit = int(digit)
        output.append(str(digit**2))
    return int(''.join(output))
