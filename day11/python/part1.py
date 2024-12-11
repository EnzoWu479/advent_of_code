def blink(arr: list[int]) -> list[int]:
    new_arr: list[int] = []
    for stone in arr:
        new_arr += transform(stone)
    return new_arr

def transform(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        middle = len(str_stone) // 2
        return [int(str_stone[:middle]), int(str_stone[middle:])]
    return [stone * 2024]

array = map(int, "4 4841539 66 5279 49207 134 609568 0".split())
for _ in range(25):
    array = blink(array)

print(len(array))