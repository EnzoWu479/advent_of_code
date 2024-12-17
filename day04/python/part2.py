import re

letters = []

def check_all_directions(y, x):
    word_diagonal_1 = ''.join([letters[y + i][x + i] for i in range(3) if y + i < len(letters) and x + i < len(letters[y + i if y + i < len(letters) else 0])])
    word_diagonal_2 = ''.join([letters[y + 2 - i][x + i] for i in range(3) if y + 2 - i < len(letters) and x + i < len(letters[y])])
    
    if (word_diagonal_1 == "MAS" or word_diagonal_1[::-1] == "MAS") and (word_diagonal_2 == "MAS" or word_diagonal_2[::-1] == "MAS"):
        return True 
    return False

# with open('input.txt') as f:
with open('./day04/input.txt') as f:
    for line in f:
        letters.append(list(line))
        
appears = 0
for y in range(len(letters) - 2):
    for x in range(len(letters[y]) - 2):
        if letters[y][x] == "M" or letters[y][x] == "S":
            cur = check_all_directions(y, x)
            if cur:
                appears += 1
print(appears)
