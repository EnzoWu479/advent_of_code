
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'

def calculate_antinodes(location1: Location, location2: Location, map_locations):
    x_diff = location2.x - location1.x
    y_diff = location2.y - location1.y 
    valid_antinodes: list[Location] = []
    antinode1 = Location(location1.x - x_diff, location1.y - y_diff)
    while True:
        if check_validity(antinode1, map_locations):
            valid_antinodes.append(antinode1)
        else:
            break
        antinode1 = Location(antinode1.x - x_diff, antinode1.y - y_diff)
    antinode2 = Location(location2.x + x_diff, location2.y + y_diff)
    while True:
        if check_validity(antinode2, map_locations):
            valid_antinodes.append(antinode2)
        else:
            break
        antinode2 = Location(antinode2.x + x_diff, antinode2.y + y_diff)
    return valid_antinodes

def check_validity(location: Location, map_locations):
    if location.x < 0 or location.y < 0:
        return False
    width = len(map_locations[0])
    height = len(map_locations)
    if location.x >= width or location.y >= height:
        return False
    return True

map_locations = []

antenas: dict[str, list[Location]] = {}

with open("input.txt") as f:
    for y, line in enumerate(f):
        map_locations.append(line.replace("\n", ""))
        for x, character in enumerate(line.replace("\n", "")):
            if character != ".":
                if character not in antenas:
                    antenas[character] = [Location(x, y)]
                else:
                    antenas[character].append(Location(x, y))

antinodes: dict[str, list[Location]] = {}
antinodes_differents = set()

for key in antenas.keys():
    antinodes[key] = [
        antinode 
        for location2 in antenas[key] 
        for location1 in antenas[key] if location1 != location2
        for antinode in calculate_antinodes(location1, location2, map_locations)
    ]
    antinodes[key] = list(set(antinodes[key]))
    [antinodes_differents.add((antinode.x, antinode.y)) for antinode in antinodes[key] + antenas[key]]

print(len(antinodes_differents))

