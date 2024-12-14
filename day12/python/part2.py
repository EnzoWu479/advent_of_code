import string
from collections import defaultdict
from typing import Self
class Location:
    def __init__(self, x: int, y: int, trail_map: list[list[str]]):
        self.x = x
        self.y = y
        self.trail_map = trail_map
        self.boundary_x = len(trail_map[0])
        self.boundary_y = len(trail_map)
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __str__(self):
        return f"(x = {self.x}, y = {self.y})"
    def __repr__(self):
        return f"(x = {self.x}, y = {self.y})"
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
    def perimeter(self):
        total = 4
        if self.top().is_valid() and self.top().get_value() == self.get_value():
            total -= 1
        if self.right().is_valid() and self.right().get_value() == self.get_value():
            total -= 1
        if self.bottom().is_valid() and self.bottom().get_value() == self.get_value():
            total -= 1
        if self.left().is_valid() and self.left().get_value() == self.get_value():
            total -= 1
        return total
    def is_connected(self, loc: Self):
        x_diff = abs(self.x - loc.x)
        y_diff = abs(self.y - loc.y)
        if x_diff == 1 and y_diff != 1:
            return True
        if y_diff == 1 and x_diff != 1:
            return True
        return False


class LetterPlot:
    def __init__(self, letter: str):
        self.locations: set[Location] = set()
        self.letter: str = letter
        pass
    def find_full_plot(self, location: Location):
        if location in self.locations:
            return
        self.locations.add(location)
        passed_locations.add(location)
        if location.top().is_valid() and location.top().get_value() == self.letter:
            self.find_full_plot(location.top())
        if location.right().is_valid() and location.right().get_value() == self.letter:
            self.find_full_plot(location.right())
        if location.bottom().is_valid() and location.bottom().get_value() == self.letter:
            self.find_full_plot(location.bottom())
        if location.left().is_valid() and location.left().get_value() == self.letter:
            self.find_full_plot(location.left())
    def area(self):
        return len(self.locations)
    def perimeter(self):
        count = 0
        for loc in self.locations:
            count += loc.perimeter()
        return count
    def sides(self):
        found_sides = []
        for location in self.locations:
            is_side = location.perimeter() > 0
            if not is_side:
                continue
            have_sides = False
            for i, side in enumerate(found_sides):
                if location.is_connected(side["location"]):
                    have_sides = True
                    found_sides[i]["sides"].append(location)
                    break
                else:
                    for s in side["sides"]:
                        if location.is_connected(s):
                            have_sides = True
                            found_sides[i]["sides"].append(location)
                            break
                if have_sides:
                    break
            if not have_sides:
                found_sides.append({
                    "location": location,
                    "sides": []
                })
        print(found_sides)
        return len(found_sides)


map_locations: list[list[str]] = []
passed_locations: set[Location] = set()
with open("input.txt") as f:
    for line in f:
        map_locations.append(list(line.replace("\n", "")))

score = 0

for y in range(len(map_locations)):
    for x in range(len(map_locations[y])):
        letter = map_locations[y][x]
        location = Location(x, y, map_locations)
        if location in passed_locations:
            continue
        letter_plot = LetterPlot(letter)
        letter_plot.find_full_plot(location)
        print(letter_plot.area(), letter_plot.sides())
        score += letter_plot.area() * letter_plot.sides()
print(score)


    