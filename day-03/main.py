import re
from typing import List


def multiply_pairs(pairs: List[List[str]]) -> List[int]:
    results = []
    do = True
    for pair in pairs:
        if pair[0] == "do()":
            do = True
            continue
        elif pair[0] == "don't()":
            do = False
            continue
        if do:
            results.append(int(pair[0]) * int(pair[1]))
    return results


def main():
    with open("day-03/input.txt") as f:
        list = [
            re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
            for line in f.readlines()
        ]

    flat_list = []
    for sublist in list:
        flat_list += sublist

    # Part One
    pairs = []
    for item in flat_list:
        matches = re.findall(r"\d{1,3}", item)
        if matches:
            pairs.append(matches)

    multiply_results = multiply_pairs(pairs)
    print(f"Sum of all products: {sum(multiply_results)}")

    # Part Two
    pairs = []
    for item in flat_list:
        matches = re.findall(r"\d{1,3}|do\(\)|don't\(\)", item)
        if matches:
            pairs.append(matches)
    multiply_results = multiply_pairs(pairs)
    print(f"Sum of all products with do/don't: {sum(multiply_results)}")
    return


if __name__ == "__main__":
    main()
