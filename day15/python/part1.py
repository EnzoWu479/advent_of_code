from typing import Self, Literal

PAREDE = "PAREDE"
CAIXA = "CAIXA"
PAREDE_CONTEUDO = "#"
CAIXA_CONTEUDO = "O"
VAZIO_CONTEUDO = "."
VAZIO = "VAZIO"
TOP = "TOP"
RIGHT = "RIGHT"
LEFT = "LEFT"
BOTTOM = "BOTTOM"

class MapLocation:
    def __init__(self, map_locations: list[list[str]]):
        self.map_locations = map_locations
        self.find_robot()

    def find_robot(self):
        found_robot = False
        for y, line in enumerate(self.map_locations):
            for x in range(len(line)):
                if self.map_locations[y][x] == "@":
                    self.robot = Robot(x, y, self)
                    found_robot = True
                    break
            if found_robot:
                break
        if not found_robot:
            raise Exception("Robot not found")

    def change_cell(self, cell, conteudo: str):
        self.map_locations[cell.y][cell.x] = conteudo
    def count_boxes(self):
        result = 0
        for y, line in enumerate(self.map_locations):
            for x, cell in enumerate(line):
                if cell == CAIXA_CONTEUDO:
                    result += 100 * y + x
        return result




class Cell:
    def __init__(self, x: int, y: int, map_location: MapLocation):
        self.x = x
        self.y = y
        self.map_location = map_location
    def classify(self):
        cell = self.get_content()
        if cell == "O":
            return CAIXA
        if cell == "#":
            return PAREDE
        return VAZIO
    def get_content(self):
        return self.map_location.map_locations[self.y][self.x]
    def move(self, direction: str):
        
        cell_target = None
        x_target = self.x
        y_target = self.y
        if direction == TOP:
            cell_target = Cell(self.x, self.y - 1, self.map_location)
            y_target = self.y - 1
        elif direction == BOTTOM:
            cell_target = Cell(self.x, self.y + 1, self.map_location)
            y_target = self.y + 1
        elif direction == RIGHT:
            cell_target = Cell(self.x + 1, self.y, self.map_location)
            x_target = self.x + 1
        elif direction == LEFT:
            cell_target = Cell(self.x - 1, self.y, self.map_location)
            x_target = self.x - 1
        if cell_target == None:
            raise Exception("Direção invalida")

        classification = cell_target.classify()
        if classification == PAREDE:
            raise Exception("Não é possivel mover uma parede")
        if classification == CAIXA:
            cell_target.move(direction)
        print(f"Moving {self.get_content()} from {self.x}, {self.y} to {x_target}, {y_target}")
        self.map_location.change_cell(Cell(x_target, y_target, self.map_location), self.get_content())
        self.map_location.change_cell(self, VAZIO_CONTEUDO)
        self.x = x_target
        self.y = y_target

class Robot(Cell):
    def __init__(self, x: int, y: int, map_location: MapLocation):
        super().__init__(x, y, map_location)

map_location_local: list[list[str]] = []
with open("./day15/map_locations.in") as f:
    for line in f:
        map_location_local.append(list(line.replace("\n", "")))

movements: list[str] = []

with open("./day15/movements.in") as f:
    for line in f:
        movements.append(line.replace("\n", ""))

map_location = MapLocation(map_location_local)
for movement_line in movements:
    for move in movement_line:
        try:
            if move == "^":
                map_location.robot.move(TOP)
            if move == ">":
                map_location.robot.move(RIGHT)
            if move == "v":
                map_location.robot.move(BOTTOM)
            if move == "<":
                map_location.robot.move(LEFT)
            # [print(line) for line in map_location.map_locations]
            # print()
            
        except:
            continue
[print(line) for line in map_location.map_locations]
print(map_location.count_boxes())