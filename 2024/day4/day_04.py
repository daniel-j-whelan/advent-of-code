char_lookup = {
    "M": 1,
    "A": 2,
    "S": 3
}

def read_input():
    with open ("input.txt") as f:
        lines = f.read().strip().split()
    return lines


def east(lines, char_lookup) -> int:
    counter = 0
    
    for line in lines:
        current_word = ""
        for char in line:
            if char == "X":
                current_word = char
                continue
            elif char in char_lookup.keys():
                if len(current_word) == char_lookup[char]:
                    current_word += char
                else:
                    current_word = ""
                if current_word == "XMAS":
                    counter += 1
                    current_word = ""
    return counter
    

def west(lines, char_lookup) -> int:
    counter = 0
    
    for line in lines:
        current_word = ""
        for char in line[::-1]:
            if char == "X":
                current_word = char
            elif char in char_lookup.keys():
                if len(current_word) == char_lookup[char]:
                    current_word += char
                else:
                    current_word = ""
                if current_word == "XMAS":
                    counter += 1
                    current_word = ""
    return counter
    
def north_west(lines) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i < 3:
            continue
        for j, char in enumerate(line):
            if j < 3:
                continue
            if char == "X" and lines[i-1][j-1] == "M" and lines[i-2][j-2] == "A" and lines[i-3][j-3] == "S":
                counter += 1
    return counter
        
    
def north_east(lines) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i < 3:
            continue
        for j, char in enumerate(line):
            if j > (len(line) - 4):
                continue
            if char == "X" and lines[i-1][j+1] == "M" and lines[i-2][j+2] == "A" and lines[i-3][j+3] == "S":
                counter += 1
    return counter
    
def south_west(lines) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i > (len(lines) - 4):
            continue
        for j, char in enumerate(line):
            if j < 3:
                continue
            if char == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                counter += 1
    return counter
    
def south_east(lines) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i > (len(lines) - 4):
            continue
        for j, char in enumerate(line):
            if j > (len(line) - 4):
                continue
            if char == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                counter += 1
    return counter

def north(lines) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i < 3:
            continue
        for j, char in enumerate(line):
            if char == "X" and lines[i-1][j] == "M" and lines[i-2][j] == "A" and lines[i-3][j] == "S":
                counter += 1
    return counter

def south(lines) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i > (len(lines) - 4):
            continue
        for j, char in enumerate(line):
            if char == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                counter += 1
    return counter


def part_one(lines: list) -> int:
    total = (
        north(lines) + north_east(lines) + north_west(lines) + south(lines) + 
        south_east(lines) + south_west(lines) + east(lines, char_lookup) + 
        west(lines, char_lookup)
    )
    return total

def part_two(lines: list) -> int:
    counter = 0
    
    for i, line in enumerate(lines):
        if i < 1 or i > (len(lines) - 2):
            continue
        for j, char in enumerate(line):
            if j < 1 or j > (len(line) - 2):
                continue
            if char == "A":
                top_left = lines[i-1][j-1]
                top_right = lines[i-1][j+1]
                bot_left = lines[i+1][j-1]
                bot_right = lines[i+1][j+1]
                if (
                    ((top_left == "S" and bot_right == "M") or (top_left == "M" and bot_right == "S")) and
                    ((top_right == "S" and bot_left == "M") or (top_right == "M" and bot_left == "S"))
                ):
                    counter += 1
    return counter