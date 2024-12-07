def is_valid(rules: dict[int, set[int]], update: list[int]) -> bool:
    for i, num in enumerate(update):
        if (
            i != len(update) - 1
            and update[i + 1] in rules
            and num in rules[update[i + 1]]
        ):
            break
        if i == len(update) - 1:
            return True
    return False


def main():
    with open("day-05/input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        sep_index = lines.index("")
        rules: dict[int, set[int]] = {}
        for rule in [rule for rule in lines[:sep_index]]:
            [key, value] = map(int, rule.split("|"))
            if key in rules:
                rules[key].add(value)
            else:
                rules[key] = {value}
        updates = [
            list(map(int, update.split(","))) for update in lines[sep_index + 1 :]
        ]
        result = 0
        for update in updates:
            if is_valid(rules, update):
                result += update[len(update) // 2]

        print(f"Result - puzzle one: {result}")
        return


if __name__ == "__main__":
    main()
