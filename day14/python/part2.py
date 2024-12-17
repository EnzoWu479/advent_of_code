FIELD_WIDTH = 101
FIELD_HEIGHT =103

QUADRANT_1 = 1
QUADRANT_2 = 2
QUADRANT_3 = 3
QUADRANT_4 = 4
QUADRANT_CENTER = None
SECONDS = 100

class Velocity:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Robot:
    def __init__(self, location: Location, velocity: Velocity):
        self.location = location
        self.velocity = velocity
    def move_in_seconds(self, seconds: int):
        self.location.x = (self.location.x + self.velocity.x * seconds) % FIELD_WIDTH
        self.location.y = (self.location.y + self.velocity.y * seconds) % FIELD_HEIGHT
    def classify_quadrant(self):
        center_x = FIELD_WIDTH // 2
        center_y = FIELD_HEIGHT // 2

        if self.location.x == center_x or self.location.y == center_y:
            return QUADRANT_CENTER
        if self.location.x < center_x and self.location.y < center_y:
            return QUADRANT_1
        if self.location.x > center_x and self.location.y < center_y:
            return QUADRANT_2
        if self.location.x < center_x and self.location.y > center_y:
            return QUADRANT_3
        if self.location.x > center_x and self.location.y > center_y:
            return QUADRANT_4

def display_map(robots: list[Robot]):
    map_locations = [["." for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]
    for robot in robots:
        map_locations[robot.location.y][robot.location.x] = "1"
    return map_locations

def get_most_robot_line_number(map_locations: list[list[str]]):
    most = 0
    for line in map_locations:
        c = line.count("1")
        if c > most:
            most = c
    return most

def write_map(second: int, map_locations: list[list[str]]):
    with open("map.txt", "a") as f:
        f.write(f"\n\nSeconds: {second}\n")
        for line in map_locations:
            f.write(f"{''.join(line)}\n")

def extract_infos(line: str):
    p_info = line.split(" ")[0].replace("p=", "").replace("\n", "")
    p_x, p_y = map(int, p_info.split(","))
    v_info = line.split(" ")[1].replace("v=", "").replace("\n", "")
    v_x, v_y = map(int, v_info.split(","))
    return p_x, p_y, v_x, v_y

robots: list[Robot] = []
with open("./day14/input.in") as f:
    for line in f:
        p_x, p_y, v_x, v_y = extract_infos(line)
        robots.append(Robot(Location(p_x, p_y), Velocity(v_x, v_y)))


for seconds in range(50000):
    for robot in robots:
        robot.move_in_seconds(1)
    most_robot_line = 0
    mapped = display_map(robots)
    line_robot = get_most_robot_line_number(mapped)
    if line_robot > 30:
        most_robot_line = line_robot
        write_map(seconds + 1, mapped)
        