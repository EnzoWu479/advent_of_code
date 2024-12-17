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

robots_classified = {
    QUADRANT_1: 0,
    QUADRANT_2: 0,
    QUADRANT_3: 0,
    QUADRANT_4: 0,
    QUADRANT_CENTER: 0,
}

for robot in robots:
    robot.move_in_seconds(SECONDS)
    classification = robot.classify_quadrant()
    robots_classified[classification] += 1
print(robots_classified)

total = 1

if robots_classified[QUADRANT_1] > 0:
    total *= robots_classified[QUADRANT_1]
if robots_classified[QUADRANT_2] > 0:
    total *= robots_classified[QUADRANT_2]
if robots_classified[QUADRANT_3] > 0:
    total *= robots_classified[QUADRANT_3]
if robots_classified[QUADRANT_4] > 0:
    total *= robots_classified[QUADRANT_4]
print(total)
    