def is_safe(nums):
    increasing = nums[0] < nums[1]
    for i in range(len(nums) - 1):
        n1, n2 = nums[i], nums[i + 1]
        diff = abs(n1 - n2)
        is_current_increasing = n1 < n2
        if n1 == n2 or diff > 3 or increasing != is_current_increasing:
            return False
    return True

number_list = []


with open('input.txt') as f:
    for line in f:
        numbers = list(map(int, line.split()))
        number_list.append(numbers)
safe = 0

for numbers in number_list:
    if is_safe(numbers):
        safe += 1
print(safe)