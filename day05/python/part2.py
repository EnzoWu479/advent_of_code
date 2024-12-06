from collections import defaultdict
from typing import List, Dict, Set

def check_and_fix_invalid_updates_and_return_middle(update: List[int], rules: Dict[int, Set[int]]) -> int:
    visited = set()
    indices = {}
    found_violation = False

    for i, page in enumerate(update):
        indices[page] = i
        intersection = rules[page].intersection(visited)

        if not intersection:
            visited.add(page)
        else:
            found_violation = True
            first_violation_index = min(indices[violation] for violation in intersection)

            # Adjust indices and rotate the problematic segment
            for p in update[first_violation_index:i]:
                indices[p] += 1

            update[first_violation_index:i+1] = update[first_violation_index:i+1][-1:] + update[first_violation_index:i]
            indices[page] = first_violation_index
            visited.add(page)

    if found_violation:
        return update[len(update) // 2]
    
    return 0

# Initialize rules
rules = defaultdict(set)

# Read rules from file
with open('input1.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.split('|'))
        rules[x].add(y)

# Read pages from file
with open('input2.txt', 'r') as file:
    pages = [list(map(int, line.split(','))) for line in file]

# Compute the result
result = sum(check_and_fix_invalid_updates_and_return_middle(update, rules) for update in pages)
print(result)