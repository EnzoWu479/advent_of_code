import re

soma = 0
with open("input.txt", "r") as f:
    for line in f:
        found = re.findall("mul\((\d+),(\d+)\)", line)
        for n1, n2 in found:
            soma += int(n1) * int(n2)
print(soma)