from typing import List


def calculate_distance(left: List[int], right: List[int]):
    total = 0
    l_copy = left[:]
    r_copy = right[:]
    while l_copy and r_copy:
        min_left = min(l_copy)
        min_right = min(r_copy)
        total += abs(min_left - min_right)
        l_copy.remove(min_left)
        r_copy.remove(min_right)
    return total


def calculate_similarity(left: List[int], right: List[int]):
    frequencies = {}
    for n in right:
        if n not in frequencies:
            frequencies[n] = 1
        else:
            frequencies[n] += 1

    score = 0
    for m in left:
        if m in frequencies:
            score += m * frequencies[m]
    return score


def main():
    with open("day-01/input.txt") as f:
        lines = f.readlines()
    cleaned_lines = [line.strip().split() for line in lines]
    left = [int(line[0]) for line in cleaned_lines]
    right = [int(line[1]) for line in cleaned_lines]

    total = calculate_distance(left, right)
    print(f"Total distance: {total}")

    score = calculate_similarity(left, right)
    print(f"Similarity score: {score}")


if __name__ == "__main__":
    main()
