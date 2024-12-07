TOP = "TOP"
BOTTOM = "BOTTOM"
LEFT = "LEFT"
RIGHT = "RIGHT"

AVAILABLE = "AVAILABLE"
OBSTACLE = "OBSTACLE"
OUT = "OUT"

class Location:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class MapLocation:
    def __init__(self, map_locations) -> None:
        self.map_locations = map_locations
        self.height = len(map_locations)
        self.width = len(map_locations[0])

    def find_player_and_direction(self):
        for y, line in enumerate(self.map_locations):
            for x, cell in enumerate(line):
                if cell in "^><v":
                    if cell == "^":
                        return Location(x, y), TOP
                    if cell == ">":
                        return Location(x, y), RIGHT
                    if cell == "v":
                        return Location(x, y), BOTTOM
                    if cell == "<":
                        return Location(x, y), LEFT
                
    def check_available_square(self, location):
        x = location.x
        y = location.y
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return OUT
        if self.map_locations[y][x] == "#":
            return OBSTACLE
        return AVAILABLE

class Player:
    def __init__(self, map_locations) -> None:
        self.passed_places = set()
        self.map_location = MapLocation(map_locations)
        self.location, self.direction = self.map_location.find_player_and_direction()

    def get_next_location(self):
        if self.direction == TOP:
            return Location(self.location.x, self.location.y - 1)
        if self.direction == RIGHT:
            return Location(self.location.x + 1, self.location.y)
        if self.direction == BOTTOM:
            return Location(self.location.x, self.location.y + 1)
        if self.direction == LEFT:
            return Location(self.location.x - 1, self.location.y)
        
    def move(self):
        next_location = self.get_next_location()
        availability = self.map_location.check_available_square(next_location)
        if availability == AVAILABLE:
            self.location = next_location
            self.passed_places.add((self.location.x, self.location.y)) 
        elif availability == OBSTACLE:
            self.turn_right()
        return availability
        
    def turn_right(self):
        if self.direction == TOP:
            self.direction = RIGHT
        elif self.direction == RIGHT:
            self.direction = BOTTOM
        elif self.direction == BOTTOM:
            self.direction = LEFT
        elif self.direction == LEFT:
            self.direction = TOP
    

def main():
    map_locations = []

    with open("input.txt") as f:
        for y, line in enumerate(f):
            map_locations.append(line.replace("\n", ""))

    player = Player(map_locations)
    while True:
        aval = player.move()
        if aval == OUT:
            break

    print(len(player.passed_places))
main()