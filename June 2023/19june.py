# CodeWars
# 19/6/2023

# Convert number to reversed array of digits
def digitize(n):
    return [int(digit) for digit in str(n)][::-1]

# You were camping with your friends far away from home, but when it's time to go back, 
# you realize that your fuel is running out and the nearest pump is 50 miles away! You 
# know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg*fuel_left >= distance_to_pump:
        return True
    return False

# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata). Strings
# passed in will consist of only letters and spaces. Spaces will be included only when more 
# than one word is present.
def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)
