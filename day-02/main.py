from typing import List


def is_decreasing(line: List[int]) -> bool:
    for i in range(len(line) - 1):
        diff = line[i] - line[i + 1]
        if diff < 1 or diff > 3:
            return False
    return True


def is_increasing(line: List[int]) -> bool:
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if diff < 1 or diff > 3:
            return False
    return True


def check_safety(line: List[int]) -> bool:
    return is_increasing(line) or is_decreasing(line)


def check_safety_with_skip(line: List[int]) -> bool:
    is_safe = check_safety(line)
    if not is_safe:
        for j in range(len(line)):
            slice = line[:j] + line[j + 1 :]
            if check_safety(slice):
                return True
    return is_safe


def main():
    with open("day-02/input.txt") as f:
        lines = f.readlines()

    safe_count = 0
    safe_count_with_skip = 0
    for line in lines:
        line = [int(n) for n in line.split()]
        if check_safety(line):
            safe_count += 1
        if check_safety_with_skip(line):
            safe_count_with_skip += 1

    print(f"Numbers of safe reports: {safe_count}")
    print(f"Numbers of safe reports with skip: {safe_count_with_skip}")
    return


if __name__ == "__main__":
    main()
