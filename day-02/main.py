from typing import List


def is_decreasing(line: List[int]):
    tmp = line[0]
    for n in line[1:]:
        diff = tmp - n
        if diff < 1 or diff > 3:
            return False
        tmp = n
    return True


def is_increasing(line: List[int]):
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


def check_safety_with_skip(line: List[int]) -> bool:
    # decrease
    if line[1] < line[0]:
        is_safe = is_decreasing(line)
        if not is_safe:
            for j in range(len(line)):
                slice = line[:j] + line[j + 1 :]
                if check_safety(slice):
                    print(slice)
                    return True
        return is_safe
    # increase
    elif line[1] > line[0]:
        is_safe = is_increasing(line)
        if not is_safe:
            count = 0
            for j in range(len(line)):
                slice = line[:j] + line[j + 1 :]
                count += 1
                if check_safety(slice):
                    print(slice)
                    return True
        return is_safe
    return False


def main():
    with open("day-02/input.txt") as f:
        lines = f.readlines()

    safe_count = 0
    safe_count_with_skip = 0
    for line in lines:
        line = line.strip().split()
        line = [int(n) for n in line]
        # if check_safety(line):
        #     safe_count += 1
        if check_safety_with_skip(line):
            print("[OK]", line)
            safe_count_with_skip += 1
        else:
            print("[NOT OK]", line)

    print(f"Numbers of safe reports: {safe_count}")
    print(f"Numbers of safe reports with skip: {safe_count_with_skip}")
    return


if __name__ == "__main__":
    main()
