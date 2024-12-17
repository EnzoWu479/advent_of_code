letters = []

def check_all_directions(y, x):
    appear_current = 0
    # Horizontal correto
    word_horizontal_correct = ''.join(letters[y][x:x+4])
    if word_horizontal_correct == "XMAS":
        appear_current += 1
    
    # Horizontal ao contrário 
    word_horizontal_backward = ''.join(letters[y][x - 3:x + 1][::-1])
    if word_horizontal_backward == "XMAS":
        appear_current += 1

    # Vertical correto
    word_vertical_correct = ''.join([letters[y + i][x] for i in range(4) if y + i < len(letters)])
    if word_vertical_correct == "XMAS":
        appear_current += 1
    
    # Vertical ao contrário
    word_vertical_backward = ''.join([letters[y - 3 + i][x] for i in range(4) if y - 3 + i >= 0])[::-1]
    if word_vertical_backward == "XMAS":
        appear_current += 1
    
    word_diagonal_1 = ''.join([letters[y + i][x + i] for i in range(4) if y + i < len(letters) and x + i < len(letters[y + i if y + i < len(letters) else 0])])
    if word_diagonal_1 == "XMAS":
        appear_current += 1
    
    word_diagonal_2 = ''.join([letters[y + 3 - i][x - 3 + i] for i in range(4) if y + 3 - i < len(letters) and x - 3 + i >= 0])[::-1]
    if word_diagonal_2 == "XMAS":
        appear_current += 1
    
    word_diagonal_3 = ''.join([letters[y - 3 + i][x + 3 - i] for i in range(4) if y - 3 + i >= 0 and x + 3 - i < len(letters[y + i if y + i < len(letters) else 0])])[::-1]
    if word_diagonal_3 == "XMAS":
        appear_current += 1
    
    word_diagonal_4 = ''.join([letters[y - 3 + i][x - 3 + i] for i in range(4) if y - 3 + i >= 0 and x - 3 + i >= 0])[::-1]
    if word_diagonal_4 == "XMAS":
        appear_current += 1

    return appear_current
    
skeleton = []

# with open('input.txt') as f:
with open('input.txt') as f:
    for line in f:
        letters.append(list(line))
appears = 0
for y in range(len(letters)):
    for x in range(len(letters[y])):
        if letters[y][x] == "X":
            cur = check_all_directions(y, x)
            appears += cur
print(appears)
