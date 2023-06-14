# CodeWars
# 14/6/2023

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
def solution(number):
    if number < 0:
        return 0

    sum_of_multiples = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum_of_multiples += num

    return sum_of_multiples

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
def pig_it(text):
    words = text.split()
    pig_words = []
    for word in words:
        if word.isalpha():
            pig_word = word[1:] + word[0] + "ay"
        else:
            pig_word = word
        pig_words.append(pig_word)
    pig_text = " ".join(pig_words)
    return pig_text