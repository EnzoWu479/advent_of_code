
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate_antinodes(location1: Location, location2: Location):
    x_diff = location2.x - location1.x
    y_diff = location2.y - location1.y 
    antinode1 = Location(location1.x - x_diff, location1.y - y_diff)
    antinode2 = Location(location2.x + x_diff, location2.y + y_diff)

    return [antinode1, antinode2]

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
        for x, character in enumerate(line):
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
        for antinode in calculate_antinodes(location1, location2) if check_validity(antinode, map_locations)
    ]
    antinodes[key] = list(set(antinodes[key]))
    [antinodes_differents.add((antinode.x, antinode.y)) for antinode in antinodes[key]]
print(len(antinodes_differents))

