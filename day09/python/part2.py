with open('input.txt', 'r') as file:
    line = []
    blanks = []
    blocks = []
    n = 0

    for i, c in enumerate(file.read()):
        if i % 2 == 1:
            line += ['.'] * int(c)
            blanks.append([int(c), n])
        else:
            line += [str(i // 2)] * int(c)
            blocks.append([int(c), n])
        n += int(c)

r = len(blocks) - 1
while r > 0:
    l = 0
    while all(a < b for a, b in zip(blanks[l], blocks[r])):
        l += 1

    if blanks[l][0] >= blocks[r][0] and blanks[l][1] < blocks[r][1]:
        for i in range(blocks[r][0]):
            line[blanks[l][1] + i], line[blocks[r][1] + i] = (
                line[blocks[r][1] + i],
                line[blanks[l][1] + i],
            )
        blanks[l][0] -= blocks[r][0]
        blanks[l][1] += blocks[r][0]

        if blanks[l][0] == 0:
            blanks.pop(l)

    r -= 1

result = sum(i * int(c) for i, c in enumerate(line) if c != '.')
print(result)
