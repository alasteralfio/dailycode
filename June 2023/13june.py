# CodeWars
# 13/6/2023

# If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    if name.startswith('r') or name.startswith("R"):
        name = name + " plays banjo" 
    else:
        name = name + " does not play banjo"
    return name

'''
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
'''
def friend(x):
    output = []
    for i in x:
        if len(i) == 4:
            output.append(i)
    return output
