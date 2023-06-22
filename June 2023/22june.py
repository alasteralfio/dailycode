# CodeWars
# 22/6/2023

# Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    count = {}
    output = []
    for number in order:
        count[number] = count.get(number, 0) + 1
        if count[number] <= max_e:
            output.append(number)
    return output

# DNA to RNA, change T to U
def dna_to_rna(dna):
    output = []
    for letter in dna:
        if letter == 'T':
            letter = 'U'
        output.append(letter)
    return ''.join(output)

# Is triangle?
def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False