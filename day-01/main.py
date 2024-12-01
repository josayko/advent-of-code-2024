from typing import List


def calculate_distance(left: List[int], right: List[int]):
    total = 0
    while left and right:
        min_left = min(left)
        min_right = min(right)
        total += abs(min_left - min_right)
        left.remove(min_left)
        right.remove(min_right)
    return total


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    cleaned_lines = [line.strip().split() for line in lines]
    left = [int(line[0]) for line in cleaned_lines]
    right = [int(line[1]) for line in cleaned_lines]

    total = calculate_distance(left, right)
    print(total)


if __name__ == "__main__":
    main()
