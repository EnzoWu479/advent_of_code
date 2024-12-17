class Button:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Prize:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Machine:
    def __init__(self, button_a: Button, button_b: Button, prize: Prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize
        self.tokens = 0
        self.current_x: int = 0
        self.current_y: int = 0

    def press_button_a(self):
        self.tokens += 3
        self.current_x += self.button_a.x
        self.current_y += self.button_a.y

    def press_button_a_multiple_times(self, times: int):
        self.tokens += 3 * times
        self.current_x += self.button_a.x * times
        self.current_y += self.button_a.y * times

    def press_button_b(self):
        self.tokens += 1
        self.current_x += self.button_b.x
        self.current_y += self.button_b.y

    def press_button_b_multiple_times(self, times: int):
        self.tokens += 1 * times
        self.current_x += self.button_b.x * times
        self.current_y += self.button_b.y * times

    def is_in_prize(self):
        return self.current_x == self.prize.x and self.current_y == self.prize.y
    
def extract_x_y_btn(line_str: str):
    x = int(line_str.split("X+")[-1].split(",")[0])
    y = int(line_str.split("Y+")[-1])
    return x, y

def extract_x_y_prize(prize_str: str):
    x = int(prize_str.split("X=")[-1].split(",")[0])
    y = int(prize_str.split("Y=")[-1])
    return x, y

def solve_linear_system(a1, b1, c1, a2, b2, c2):
    new_b1 = b1 * a2
    new_b2 = b2 * a1
    new_c1 = c1 * a2
    new_c2 = c2 * a1
    
    b_coef = new_b2 - new_b1
    c_constant = new_c2 - new_c1

    B = c_constant / b_coef
    A = (c1 - b1 * B) / a1
    
    return A, B

lines = []

with open("input.in") as f:
    for line in f:
        lines.append(line.replace("\n", ""))

btn_str_a = ""
btn_str_b = ""
prize_str = ""

tokens = 0
for line in lines:
    if "A" in line:
        btn_str_a = line
    elif "B" in line:
        btn_str_b = line
    elif "Prize" in line:
        prize_str = line
    if btn_str_a and btn_str_b and prize_str:
        x_a, y_a = extract_x_y_btn(btn_str_a)
        x_b, y_b = extract_x_y_btn(btn_str_b)
        x_p, y_p = extract_x_y_prize(prize_str)
        x_p, y_p = x_p + 10000000000000, y_p + 10000000000000
        btn_str_a = ""
        btn_str_b = ""
        prize_str = ""

        a, b = solve_linear_system(x_a, x_b, x_p, y_a, y_b, y_p)
        
        if a < 0 or b < 0 or not a.is_integer() or not b.is_integer():
            continue
        tokens += a * 3 + b
print(int(tokens))

