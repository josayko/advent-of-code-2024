from typing import List


def is_decreasing(line: List[int]) -> bool:
    tmp = line[0]
    for n in line[1:]:
        diff = tmp - n
        if diff < 1 or diff > 3:
            return False
        tmp = n
    return True


def is_increasing(line: List[int]) -> bool:
    tmp = line[0]
    for n in line[1:]:
        diff = n - tmp
        if diff < 1 or diff > 3:
            return False
        tmp = n
    return True


def check_safety(line: List[int]) -> bool:
    # decrease
    if line[1] < line[0]:
        return is_decreasing(line)
    # increase
    elif line[1] > line[0]:
        return is_increasing(line)
    return False


def main():
    with open("day-02/input.txt") as f:
        lines = f.readlines()

    safe_count = 0
    for line in lines:
        line = line.strip().split()
        line = [int(n) for n in line]
        if check_safety(line):
            safe_count += 1

    print(f"Numbers of safe reports: {safe_count}")
    return


if __name__ == "__main__":
    main()
