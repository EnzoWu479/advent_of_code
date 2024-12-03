import re

soma_total = 0
valid = True

def sum_valid(found_indexes):
    soma = 0
    global valid
    for found in found_indexes:
        if found["type"] == "do":
            valid = True
        elif found["type"] == "dont":
            valid = False
        else:
            if valid:
                line_cut = line[found["i"]:]
                mul_match = re.search("mul\((\d+),(\d+)\)", line_cut)
                n1, n2 = map(int, line_cut[4:mul_match.end() - 1].split(","))
                soma += n1 * n2
    return soma

with open("input.txt", "r") as f:
    for line in f:
        found_mul = [m.start(0) for m in re.finditer("mul\((\d+),(\d+)\)", line)]
        found_dont = [m.start(0) for m in re.finditer("don't\(\)", line)]
        fount_do = [m.start(0) for m in re.finditer("do\(\)", line)]

        unique_found = \
            [{"i": i, "type": "mul"} for i in found_mul] + \
            [{"i": i, "type": "dont"} for i in found_dont] + \
            [{"i": i, "type": "do"} for i in fount_do]
        
        unique_found.sort(key=lambda x : x["i"])
        soma_total += sum_valid(unique_found)
print(soma_total)