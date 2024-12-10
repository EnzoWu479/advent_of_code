with open('inputtest.txt') as f:
    for line in f:
        diskmap = line

empty = False
count = 0
main_blocks = []

for index, character in enumerate(list(diskmap)[::-1]):
    main_blocks.append({
        "index": index,
        "size": int(character),
        "value": count if not empty else None
    })
    if not empty:
        count += 1
    empty = not empty

files = list(filter(lambda x : x["value"] != None, main_blocks))
files.sort(key=lambda x : x["value"], reverse=True)

soma = 0
last_num_index = 0
for i, block in enumerate(main_blocks):
    is_empty = block["value"] == None
    if is_empty:
        biggest_that_fit = None
        for file in files:
            if file["size"] <= block["size"]:
                biggest_that_fit = file
                break
        if biggest_that_fit != None:
            num = main_blocks[numbr_blocks[-last_num_index-1]]
        last_num_index += 1
    else:
        num = block["value"]
    soma += i * num
print(soma)