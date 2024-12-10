class Location:
    def __init__(self, x: int, y: int, trail_map: list[list[int]]):
        self.x = x
        self.y = y
        self.trail_map = trail_map
        self.boundary_x = len(trail_map[0])
        self.boundary_y = len(trail_map)
    def top(self):
        return Location(self.x, self.y - 1, self.trail_map)
    def right(self):
        return Location(self.x + 1, self.y, self.trail_map)
    def bottom(self):
        return Location(self.x, self.y + 1, self.trail_map)
    def left(self):
        return Location(self.x - 1, self.y, self.trail_map)
    def is_valid(self):
        if self.x < 0 or self.y < 0:
            return False
        if self.x >= self.boundary_x or self.y >= self.boundary_y:
            return False
        return True 
    def get_value(self):
        return self.trail_map[self.y][self.x]
    

def search_sequence(location: Location, search_number: int, found: set[tuple[int]]):
    if search_number > 9:
        key = (location.x, location.y)
        if key not in found:
            found.add((location.x, location.y))
            return 1
        return 0
    total: int = 0
    if location.top().is_valid() and location.top().get_value() == search_number:
        total += search_sequence(location.top(), search_number + 1, found)
    if location.right().is_valid() and location.right().get_value() == search_number:
        total += search_sequence(location.right(), search_number + 1, found)
    if location.bottom().is_valid() and location.bottom().get_value() == search_number:
        total += search_sequence(location.bottom(), search_number + 1, found)
    if location.left().is_valid() and location.left().get_value() == search_number:
        total += search_sequence(location.left(), search_number + 1, found)
    return total
    


trail = []

with open("input.txt") as f:
    for line in f:
        trail.append(list(map(int, list(line.replace("\n", "")))))
total = 0
for y, line in enumerate(trail):
    for x, cell in enumerate(line):
        if cell == 0:
            found_set = set()
            found = search_sequence(Location(x, y, trail), 1, found_set)
            total += found
print(total)   
