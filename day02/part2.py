def is_safe(nums):
    increasing = nums[0] < nums[1]
    for i in range(len(nums) - 1):
        n1, n2 = nums[i], nums[i + 1]
        diff = abs(n1 - n2)
        is_current_increasing = n1 < n2
        if n1 == n2 or diff > 3 or increasing != is_current_increasing:
            return False
    return True

def is_safe_removing_i(nums, i=0):
    if i == len(nums):
        return False
    nums_copy = nums.copy()
    nums_copy.pop(i)
    if is_safe(nums_copy):
        return True
    return is_safe_removing_i(nums, i + 1)

number_list = []


with open('input.txt') as f:
    for line in f:
        numbers = list(map(int, line.split()))
        number_list.append(numbers)

safe = 0

for numbers in number_list:
    if is_safe_removing_i(numbers):
        safe += 1
print(safe)