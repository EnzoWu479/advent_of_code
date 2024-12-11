from collections import Counter

def blink(arr_counted: Counter[int]) -> Counter[int]:
    new_counts = Counter()
    for stone, count in arr_counted.items():
        transformed = transform(stone)
        for t in transformed:
            new_counts[t] += count
    return new_counts


def transform(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        middle = len(str_stone) // 2
        return  [int(str_stone[:middle]), int(str_stone[middle:])]
    return [stone * 2024]

array = map(int, "4 4841539 66 5279 49207 134 609568 0".split())
count_values = Counter(array)

for a in range(75):
    count_values = blink(count_values)

print(sum(count_values.values()))