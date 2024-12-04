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
    safe_count = 0
    
    for report in [line.split(" ") for line in lines]:
        safe = True
        ascending = []
        for i in range(1, len(report)):
            if (abs(int(report[i]) - int(report[i-1])) > 3) or (int(report[i]) == int(report[i-1])):
                safe = False
                break
            ascending.append(True) if int(report[i]) > int(report[i-1]) else ascending.append(False)
        if (all(ascending) or not any(ascending)) and safe:
            safe_count += 1
  

def part_two(lines: list) -> int:
    """solution to part two

    Args:
        lines (list): the basic input file parsed into a list

    Returns:
        score (int): the similarity score between the left and right lists
    """
    left_ids, right_ids = ([line.split("   ")[i] for line in lines] for i in (0,1))

    score = 0
    right_counts = {}
    for location_id in right_ids:
        right_counts[location_id] = right_counts.get(location_id, 0) + 1

    for location_id in left_ids:
        score += right_counts.get(location_id, 0) * int(location_id)
   
    return score