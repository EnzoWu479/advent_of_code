def is_valid(arr, restricts, i=0):
    if i == len(arr):
        return True
    current = arr[i]
    after = arr[i:]
    if current in restricts:
        for value in after:
            if value not in restricts[current]["after"] and value in restricts[current]["before"]:
                return False
    return is_valid(arr, restricts, i + 1)

def get_center_value(arr):
    center_index = len(arr) // 2 
    return arr[center_index]

restrictions = {}

with open("input1.txt") as f:
    for line in f:
        n1, n2 = map(int, line.split("|"))
        if n1 not in restrictions:
            restrictions[n1] = {
                "before": set(),
                "after": set([n2])
            }
        else:
            restrictions[n1]["after"].add(n2)
        if n2 not in restrictions:
            restrictions[n2] = {
                "before": set([n1]),
                "after": set()
            }
        else:
            restrictions[n2]["before"].add(n1)

soma = 0

with open("input2.txt") as f:
    for line in f:
        test_case = list(map(int, line.split(",")))
        if is_valid(test_case, restrictions):
            center_value = get_center_value(test_case)
            soma += center_value
print(soma)