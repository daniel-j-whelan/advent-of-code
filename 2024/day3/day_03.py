import re

def read_input() -> list:
    """read the basic input file
    
    Args:
        None

    Returns:
        lines (list): the basic input file parsed into a list
    """
    with open ("input.txt") as f:
        lines = f.read().strip().split("\n")
        
    return lines


def part_one(lines: list) -> int:
    """solution to part one

    Args:
        lines (list): the basic input file parsed into a list

    Returns:
        distance (int): the total distance between the left and right lists
    """
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    number_pattern = r"\d{1,3}"
    mul_matches = re.findall(mul_pattern, lines)

    for match in mul_matches:
        left, right = re.findall(number_pattern, match)
        total += int(left) * int(right)
        
    return total

  

def part_two(lines: list) -> int:
    """solution to part two

    Args:
        lines (list): the basic input file parsed into a list

    Returns:
        score (int): the similarity score between the left and right lists
    """
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    number_pattern = r"\d{1,3}"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    all_patterns = f"{mul_pattern}|{do_pattern}|{dont_pattern}"
    all_matches = re.findall(all_patterns, lines)

    enabled_total = 0
    dont = False
    for match in all_matches:
        if match == "don't()":
            dont = True
            continue
        elif match == "do()":
            dont = False
            continue

        if dont == False:
            print(match)
            left, right = re.findall(number_pattern, match)
            enabled_total += int(left) * int(right)
    return enabled_total