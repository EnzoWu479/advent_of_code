with open('input.txt') as f:
    for line in f:
        diskmap = line

empty = False
count = 0
numbr_blocks = []
empty_blocks = []
main_blocks = []

for index, character in enumerate(list(diskmap)):
    main_blocks += ["." if empty else count for _ in range(int(character))] 
    if empty:
        empty_blocks += [i for i in range(len(main_blocks) - int(character), len(main_blocks))] 
    else:
        numbr_blocks += [i for i in range(len(main_blocks) - int(character), len(main_blocks))] 
        count += 1
    empty = not empty

soma = 0
last_num_index = 0
for i, n in enumerate(main_blocks):
    if i > numbr_blocks[-last_num_index-1]:
        break 
    if n == ".":
        num = main_blocks[numbr_blocks[-last_num_index-1]]
        last_num_index += 1
    else:
        num = n
    soma += i * num
print(soma)